import math

def cosine_similarity(vec1, vec2):
    dot_product = sum(a*b for a, b in zip(vec1, vec2))
    norm_a = math.sqrt(sum(a*a for a in vec1))
    norm_b = math.sqrt(sum(b*b for b in vec2))
    return dot_product / (norm_a * norm_b)

def smart_chunk_text(text: str, max_chunk_size=1500):
    """
    Splits text intelligently without breaking meaning
    """
    lines = text.split("\n")
    chunks = []
    current_chunk = ""

    for line in lines:
        if len(current_chunk) + len(line) < max_chunk_size:
            current_chunk += line + "\n"
        else:
            chunks.append(current_chunk)
            current_chunk = line + "\n"

    if current_chunk:
        chunks.append(current_chunk)

    return chunks
def get_reference_texts():
    return [
        "API failure error exception timeout issue",
        "database connection failure refused timeout",
        "authentication authorization login failure",
        "server error 500 internal server issue",
        "network issue DNS timeout connection problem",
        "validation error bad request missing fields",
        "performance issue slow response latency",
        "unexpected system crash null pointer exception",
        "permission denied unauthorized access error"
    ]

def get_reference_embeddings(ai_client):
    texts = get_reference_texts()
    return [ai_client.get_embedding(text) for text in texts]


def filter_logs_with_embeddings(log_text, ai_client, threshold=0.7):
    reference_embeddings = get_reference_embeddings(ai_client)

    important_lines = []

    for line in log_text.split("\n"):
        if not line.strip():
            continue

        line_embedding = ai_client.get_embedding(line)

        # Compare with ALL categories
        similarities = [
            cosine_similarity(line_embedding, ref_emb)
            for ref_emb in reference_embeddings
        ]

        max_similarity = max(similarities)

        if max_similarity > threshold:
            important_lines.append(line)

    return "\n".join(important_lines)

def refine_logs_with_ai(filtered_logs, ai_client):
    prompt = f"""
    You are a QA expert.

    From the following logs:
    - Keep only critical errors
    - Remove duplicates
    - Ignore noise

    Return clean log lines only.

    Logs:
    {filtered_logs}
    """

    return ai_client.generate_text(prompt)