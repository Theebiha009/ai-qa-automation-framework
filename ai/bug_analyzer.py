import json
from ai.smart_processor import (
    filter_logs_with_embeddings,
    refine_logs_with_ai,
    smart_chunk_text
)
from ai.bug_similarity import BugSimilarity


# ✅ Helper: Clean AI JSON output
def clean_json_response(text: str) -> str:
    text = text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    if text.lower().startswith("here is"):
        text = text.split("\n", 1)[-1]

    return text


def analyze_large_logs(log_text, ai_client):

    # Step 1: Semantic filtering
    filtered_logs = filter_logs_with_embeddings(log_text, ai_client)

    # Step 2: Fallback
    if not filtered_logs:
        filtered_logs = log_text[:2000]

    # Step 3: AI refinement
    refined_logs = refine_logs_with_ai(filtered_logs, ai_client)

    # Step 4: Chunking
    chunks = smart_chunk_text(refined_logs)

    results = []

    # Step 5: Analyze each chunk
    for chunk in chunks:
        prompt = f"""
        You are a QA expert.

        Analyze the log and return ONLY valid JSON.

        Format:
        {{
            "root_cause": "",
            "error_type": "",
            "severity": ""
        }}

        Log:
        {chunk}
        """

        result = ai_client.generate_text(prompt)
        results.append(result)

    # ✅ Step 6: UPDATED FINAL PROMPT (YOUR QUESTION 🔥)
    final_prompt = f"""
    Combine these analyses into ONE final JSON.

    IMPORTANT:
    - Return ONLY valid JSON
    - Do NOT include ``` or explanations
    - Output must be directly parsable

    Format:
    {{
        "root_cause": "",
        "error_type": "",
        "severity": ""
    }}

    Data:
    {results}
    """

    final_result = ai_client.generate_text(final_prompt)
    print("FINAL RAW:", final_result)
    # ✅ Step 7: CLEAN + PARSE JSON
    cleaned = clean_json_response(final_result)
    print("CLEANED:", cleaned)
    try:
        parsed = json.loads(cleaned)
    except Exception:
        return {
            "status": "ERROR",
            "message": "Invalid JSON from AI",
            "raw_output": final_result
        }

    # ✅ Step 8: Extract root cause
    description = parsed.get("root_cause", "").strip()

    if not description:
        description = cleaned[:200]

    # ✅ Step 9: Duplicate detection
    similarity_engine = BugSimilarity(ai_client)

    duplicate_check = similarity_engine.find_duplicate(description)

    if duplicate_check["duplicate"]:
        return {
            "status": "DUPLICATE",
            "analysis": parsed,
            "matched_bug": duplicate_check["matched_bug"],
            "similarity": duplicate_check["similarity"]
        }

    else:
        new_bug = similarity_engine.save_new_bug(
            description,
            duplicate_check["embedding"]
        )

        return {
            "status": "NEW_BUG",
            "analysis": parsed,
            "bug": new_bug
        }