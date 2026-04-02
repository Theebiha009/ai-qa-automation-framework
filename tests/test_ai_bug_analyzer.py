import json
from ai.ai_client import AIClient
from ai.prompts import bug_analysis_prompt_json

def test_ai_bug_analysis_json():
    ai = AIClient()

    # Read JSON logs
    with open("reports/test_logs.json", "r") as f:
        logs = json.load(f)

    prompt = bug_analysis_prompt_json(logs)

    result = ai.generate_text(prompt)

    print(result)

    # Save AI output
    with open("reports/ai_bug_report.json", "w", encoding="utf-8") as f:
        f.write(result)

    assert result is not None