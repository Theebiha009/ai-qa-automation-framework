# 🤖 AI-Powered QA Automation Framework

An advanced API automation framework integrating **AI, embeddings, and intelligent bug analysis**. This project demonstrates how modern QA can evolve from traditional automation to **AI-driven quality engineering**.

---

## 🚀 Features

### ✅ Core Automation

* Pytest-based API automation framework
* Parallel execution using pytest-xdist
* Data-driven testing (JSON/CSV support)
* Modular and scalable architecture

### 🤖 AI Capabilities

* AI Test Case Generator (prompt-based)
* Swagger → Pytest script generation
* AI Bug Analyzer (log → root cause → severity)
* Embedding-based duplicate bug detection

### 📊 Reporting & Debugging

* Allure reporting integration
* JSON-based result storage
* Individual test run tracking
* Structured logs for debugging

---

## 🧠 AI Architecture

```
Logs → AI Analysis → Root Cause → Embedding → Similarity Check → Duplicate Detection
```

---

## 📂 Project Structure

```
ai/
  ai_client.py
  bug_analyzer.py
  bug_similarity.py
  swagger_test_generator.py

utils/
  logger.py

tests/
  test_bug_similarity.py

data/
  bug_store.json

reports/
  allure-results/

generated_tests/   (AI-generated tests, excluded from pytest)
```

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/Theebiha009/ai-qa-automation-framework.git
cd ai-qa-automation-framework
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in root directory:

```
OPENAI_API_KEY=your_openai_api_key
```

(Optional for future integrations)

```
JIRA_EMAIL=your_email
JIRA_API_TOKEN=your_token
```

---

## ▶️ Run Tests

Run all tests:

```bash
pytest -v -s
```

Run in parallel:

```bash
pytest -n auto
```

Run specific test:

```bash
pytest tests/test_bug_similarity.py -v
```

---

## 📊 Allure Reporting

Generate results:

```bash
pytest --alluredir=reports/allure-results
```

View report:

```bash
allure serve reports/allure-results
```

---

## 🧪 Example Use Cases

* Analyze API failures using AI and extract root cause
* Detect duplicate bugs using embeddings (semantic similarity)
* Generate automated test scripts from Swagger/OpenAPI
* Store and track bug analysis results over time

---

## 🧠 Key Concepts Used

* LLM Prompt Engineering
* Embeddings & Semantic Search
* Cosine Similarity
* AI-based Test Generation
* Parallel Test Execution
* Data-driven Testing

---

## 🎯 Why this project?

This framework showcases how AI can enhance QA workflows by:

* Reducing manual debugging effort
* Preventing duplicate bug creation
* Automatically generating test scenarios
* Improving test intelligence and efficiency

---

## 👤 Author

**Theebiha Jeyashankar**

---

## ⭐ Future Enhancements

* Jira integration for auto bug creation
* Vector database (FAISS / Pinecone)
* CI/CD pipeline integration (GitHub Actions / Azure DevOps)
* Dashboard for bug analytics

---
