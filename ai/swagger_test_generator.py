from ai.ai_client import AIClient
from ai.prompts import swagger_to_tests_prompt
import re

class SwaggerTestGenerator:

    def __init__(self):
        self.ai = AIClient()

    def generate_tests(self, swagger_text, filename):
        prompt = swagger_to_tests_prompt(swagger_text)

        result = self.ai.generate_text(prompt)

        # ✅ Clean AI output
        cleaned_code = self.clean_generated_code(result)

        with open(f"generated_tests/{filename}", "w", encoding="utf-8") as f:
            f.write(cleaned_code)

        return cleaned_code

    @staticmethod
    def clean_generated_code(code: str) -> str:
        # Remove markdowns blocks
        code = re.sub(r"```python", "", code)
        code = re.sub(r"```", "", code)

        # Remove leading/trailing spaces
        return code.strip()