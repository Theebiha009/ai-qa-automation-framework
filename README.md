# 🤖 AI-Powered QA Automation Framework

A scalable **API test automation framework** built using **Python + pytest**, enhanced with **AI capabilities** for intelligent test generation and failure analysis.

---

# 🚀 Key Features

* ✅ API Automation using pytest & requests
* ✅ Parallel execution using pytest-xdist
* ✅ Data-driven testing (JSON & CSV)
* ✅ Schema validation using jsonschema
* ✅ Async API testing using aiohttp

### 🤖 AI Capabilities

* 🔥 Generate pytest scripts from Swagger/OpenAPI
* 🔥 AI Bug Analyzer (logs → root cause insights)

---

# 🧱 Project Structure

```
ai-qa-automation-framework/
│
├── tests/                  # Stable test cases
├── generated_tests/        # AI-generated tests (isolated)
├── api/                    # API client & endpoints
├── ai/                     # AI modules (generator, analyzer)
├── utils/                  # Helpers & logging
├── config/                 # Configuration handling
├── data/                   # Test data (JSON/CSV)
├── reports/                # Allure reports & logs
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone repository

```
git clone <your-repo-url>
cd ai-qa-automation-framework
```

## 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate   # Windows
```

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

# 🔐 Configuration

Set environment variables:

```
OPENAI_API_KEY=your_api_key
BASE_URL=https://restful-booker.herokuapp.com
```

---

# 🧪 Running Tests

## Run stable tests

```
pytest tests/
```

## Run in parallel

```
pytest -n auto tests/
```

## Run AI-generated tests (optional)

```
pytest generated_tests/
```


---

# 🤖 AI Features

## 1. AI Test Generator

**Input:** Swagger / API definition
**Output:** Executable pytest scripts

Example:

```
generator.generate_tests(swagger_text, "test_swagger_booking.py")
```

---

## 2. AI Bug Analyzer

**Input:** Failure logs
**Output:**

* Root cause
* Grouped issues
* Insights

---

# ⚡ Async API Testing

Supports high-performance API testing using:

```
aiohttp
async/await
```

---

# 🧠 Design Highlights

* Clean modular architecture
* Reusable API client
* Separation of stable vs AI tests
* AI-assisted automation workflows

---

# 📈 Why This Project?

This framework demonstrates:

* Real-world API automation
* Scalable test design
* Integration of AI into QA workflows
* Parallel & async execution



---

# 🙌 Author

Theebiha Jeyashankar
QA Automation Engineer | AI in Testing Enthusiast
