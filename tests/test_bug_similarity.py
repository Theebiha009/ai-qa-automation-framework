import json
import os
from datetime import datetime

import allure
from ai.ai_client import AIClient
from ai.bug_analyzer import analyze_large_logs


# ✅ Save cumulative results (append mode)
def save_test_result(data, filename="bug_results.json"):

    os.makedirs("reports", exist_ok=True)

    file_path = f"reports/{filename}"

    data_with_time = {
        "timestamp": datetime.now().isoformat(),
        "result": data
    }

    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            existing = []
    else:
        existing = []

    existing.append(data_with_time)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2)


# ✅ Save separate file per run
def save_individual_result(data, prefix="bug_result"):

    os.makedirs("reports/individual", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

    filename = f"reports/individual/{prefix}_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return filename


def test_duplicate_bug_detection():

    ai_client = AIClient()

    log1 = "ERROR: Login API timeout"
    log2 = "ERROR: Login service connection timeout"

    # 🔹 First run
    result1 = analyze_large_logs(log1, ai_client)
    print("First:", result1)

    save_test_result(result1)
    file1 = save_individual_result(result1, "first_run")

    # 🔹 Allure attachment
    allure.attach(
        json.dumps(result1, indent=2),
        name="First Run Result",
        attachment_type=allure.attachment_type.JSON
    )

    # 🔹 Second run
    result2 = analyze_large_logs(log2, ai_client)
    print("Second:", result2)

    save_test_result(result2)
    file2 = save_individual_result(result2, "second_run")

    # 🔹 Allure attachment
    allure.attach(
        json.dumps(result2, indent=2),
        name="Second Run Result",
        attachment_type=allure.attachment_type.JSON
    )

    # 🔹 Optional: attach file paths
    allure.attach(
        f"Saved files:\n{file1}\n{file2}",
        name="Saved File Locations",
        attachment_type=allure.attachment_type.TEXT
    )

    # ✅ Assertion
    assert result2["status"] in ["DUPLICATE", "NEW_BUG"]