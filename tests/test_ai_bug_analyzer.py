import json
from ai.ai_client import AIClient
from ai.prompts import bug_analysis_prompt_json
import allure
from ai.bug_analyzer import analyze_large_logs

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

@allure.title("AI Bug Analysis Test")
@allure.description("Validate AI-based log analysis")
def test_ai_bug_analysis_with_sample_logs():
    ai_client = AIClient()

    log_text = """
    INFO: User logged in successfully
    ERROR: Timeout while connecting to DB
    WARNING: Retrying request
    ERROR: Connection refused
    """

    result = analyze_large_logs(log_text, ai_client)

    print("AI Result:", result)

    # Convert to JSON (important)
    parsed = json.loads(result)

    # ✅ Validations
    assert "root_cause" in parsed
    assert "error_type" in parsed
    assert "severity" in parsed

    # ✅ Attach to Allure
    allure.attach(
        json.dumps(parsed, indent=2),
        name="AI Bug Analysis",
        attachment_type=allure.attachment_type.JSON
    )

def test_ai_bug_analysis_from_file():
    ai_client = AIClient()

    with open("data/logs.txt", "r", encoding="utf-8") as f:
        log_text = f.read()

    result = analyze_large_logs(log_text, ai_client)

    parsed = json.loads(result)

    assert parsed["root_cause"] != ""

def test_ai_bug_analysis_unknown_errors():
    ai_client = AIClient()

    log_text = """
    INFO: User logged in
    ERROR: DB handshake failed
    WARNING: retrying connection
    ERROR: upstream service crashed unexpectedly
    """

    result = analyze_large_logs(log_text, ai_client)

    print("AI Output:", result)

    parsed = json.loads(result)

    assert "root_cause" in parsed
    assert "error_type" in parsed
    assert "severity" in parsed
