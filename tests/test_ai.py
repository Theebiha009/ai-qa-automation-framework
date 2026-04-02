from ai.ai_client import AIClient
import time
from ai.prompts import generate_test_cases_prompt
from ai.prompts import user_story_to_testcases_prompt
from ai.swagger_test_generator import SwaggerTestGenerator


def test_generate_login_test_cases():
    ai = AIClient()

    prompt = generate_test_cases_prompt("Login API")

    result = ai.generate_text(prompt)

    print("\nAI Generated Test Cases:\n")
    print(result)

    assert result is not None

def test_user_story_to_testcases():
    ai = AIClient()

    user_story = """
    User logs in with username and password.
    Invalid password should show error.
    Lock account after 5 failed attempts.
    """

    prompt = user_story_to_testcases_prompt(user_story)

    result = ai.generate_text(prompt)

    print("\nGenerated Test Cases:\n")
    print(result)

    assert "Test Case" in result
    # ✅ Save AI output to file
    filename = f"reports/ai_output_{int(time.time())}.txt"

    with open(filename, "w") as f:
        f.write(result)

def test_generate_swagger_tests():
    generator = SwaggerTestGenerator()

    swagger = """
    POST /booking

    Request Body:
    {
      "firstname": "string",
      "lastname": "string",
      "totalprice": 100,
      "depositpaid": true,
      "bookingdates": {
        "checkin": "YYYY-MM-DD",
        "checkout": "YYYY-MM-DD"
      },
      "additionalneeds": "string"
    }

    Response:
    {
      "bookingid": 1,
      "booking": {
        "firstname": "string",
        "lastname": "string",
        "totalprice": 100,
        "depositpaid": true,
        "bookingdates": {
          "checkin": "string",
          "checkout": "string"
        }
      }
    }
    """

    generator.generate_tests(swagger, "test_swagger_booking.py")