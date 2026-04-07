import json
import os
import math


class BugSimilarity:

    def __init__(self, ai_client, db_path="data/bug_store.json"):
        self.ai = ai_client
        self.db_path = db_path

        if not os.path.exists(self.db_path):
            with open(self.db_path, "w") as f:
                json.dump([], f)

    # 🔹 Load existing bugs
    def load_bugs(self):
        with open(self.db_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # 🔹 Save bugs
    def save_bugs(self, bugs):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(bugs, f, indent=2)

    # 🔹 Cosine similarity
    def cosine_similarity(self, v1, v2):
        dot = sum(a*b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a*a for a in v1))
        norm2 = math.sqrt(sum(b*b for b in v2))
        return dot / (norm1 * norm2)

    # 🔥 Check duplicate
    def find_duplicate(self, description, threshold=0.85):
        bugs = self.load_bugs()

        new_embedding = self.ai.get_embedding(description)

        for bug in bugs:
            similarity = self.cosine_similarity(new_embedding, bug["embedding"])

            if similarity > threshold:
                return {
                    "duplicate": True,
                    "matched_bug": bug,
                    "similarity": similarity
                }

        return {
            "duplicate": False,
            "embedding": new_embedding
        }

    # 🔥 Save new bug
    def save_new_bug(self, description, embedding):
        bugs = self.load_bugs()

        new_bug = {
            "id": f"BUG-{len(bugs)+1}",
            "description": description,
            "embedding": embedding
        }

        bugs.append(new_bug)
        self.save_bugs(bugs)

        return new_bug