def generate_test_cases_prompt(feature):
    return f"""
    You are a QA engineer.

    Generate API test cases for:
    {feature}

    Include:
    - Positive cases
    - Negative cases
    - Edge cases

    Format:
    Test Case ID:
    Description:
    Steps:
    Expected Result:
    """

def user_story_to_testcases_prompt(user_story):
    return f"""
    You are a senior QA engineer.

    Convert the following user story into detailed API test cases:

    {user_story}

    Include:
    - Functional scenarios
    - Negative cases
    - Edge cases
    - Security considerations

    Output in structured format.
    """

def bug_analysis_prompt_json(logs):
    return f"""
    You are a senior QA engineer.

    Analyze the following JSON logs:

    {logs}

    Tasks:
    1. Group failures by API
    2. Identify common error types
    3. Suggest root causes

    Return JSON format:
    [
      {{
        "api": "",
        "issue": "",
        "root_cause": "",
        "recommendation": ""
      }}
    ]
    """

def swagger_to_tests_prompt(swagger_text):
    return f"""
    You are a QA automation engineer.

    Generate pytest API tests based on this Swagger API:

    {swagger_text}

    Requirements:
    - Use APIClient class
    - Use pytest
    - Add assertions for status codes
    - Include positive and negative scenarios

    Output ONLY Python code.
    """