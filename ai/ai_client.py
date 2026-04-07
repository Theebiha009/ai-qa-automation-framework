from openai import OpenAI
import os

class AIClient:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_text(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0,  # ✅ IMPORTANT
            top_p=1  # ✅ keep default
        )

        return response.choices[0].message.content

    def get_embedding(self, text: str):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding

    def get_embeddings_batch(ai_client, texts):
        response = ai_client.client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        return [item.embedding for item in response.data]