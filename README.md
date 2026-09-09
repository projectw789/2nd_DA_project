# AI-Powered Job Application Intelligence & Automation System

A Python application that uses an LLM to analyse how well a candidate matches a job, calculates a deterministic suitability score, and stores the analysis in a SQLite database.

This project was built as a software-engineering portfolio project to explore how AI can be integrated into a wider software system using conventional engineering practices such as data validation, modular design, business logic, persistence, APIs, error handling, and automated testing.

## Project Overview

The application takes:

* Company
* Job role
* Job description
* Candidate profile

It then processes the application through a series of stages:

```text
Job application input
        │
        ▼
Pydantic validation
        │
        ▼
LLM analysis via OpenRouter
        │
        ▼
Structured AI response
        │
        ▼
Pydantic validation
        │
        ▼
Deterministic suitability scoring
        │
        ▼
Final analysis
        │
        ├──────────────► CLI output
        │
        ├──────────────► SQLite database
        │
        └──────────────► FastAPI API
```

The key design principle is that the LLM is used for **qualitative analysis**, while the final numerical score is calculated by conventional Python code using fixed rules.

## Key Engineering Features

### Structured data validation

User input is validated with Pydantic before entering the analysis pipeline.

The LLM response is also parsed as JSON and validated against a Pydantic model before being passed to the rest of the application.

This reduces the risk of the rest of the system receiving unexpected data structures.

### Deterministic business logic

The LLM identifies job requirements and compares them with the candidate profile, but it does not decide the final suitability score.

The score is calculated using explicit Python logic:

| Category         | Maximum points |
| ---------------- | -------------: |
| Skills match     |             50 |
| Experience match |             30 |
| Education match  |             20 |
| **Total**        |        **100** |

The skills component is based on the proportion of matched skills to key requirements.

Keeping this logic outside the LLM makes the scoring rules explicit, reproducible, and easier to test.

### API integration

The application integrates with an external LLM through OpenRouter using an OpenAI-compatible client.

The project also exposes the analysis system through FastAPI, allowing it to be used through HTTP requests rather than only from the command line.

### Database persistence

Completed analyses are stored in SQLite.

List-based information such as requirements and skills is serialised as JSON before being stored and reconstructed when retrieved.

The database layer uses fresh SQLite connections for database operations rather than relying on one global connection, which also avoids the threading issue encountered when the application was exposed through FastAPI.

### Automated testing

The project uses pytest to test important application behaviour.

The current test suite contains 7 tests covering:

* Multiple suitability-score scenarios
* `choice()` behaviour when no AI response is available
* Successful conversion of AI output into the final output model
* Valid user input
* User-input retry behaviour when an empty field is entered

Run the tests with:

```bash
uv run pytest
```

## API

The application exposes two FastAPI endpoints.

### `POST /analyse`

Accepts a JSON job application, runs the analysis pipeline, saves the result to the database, and returns the final analysis.

### `GET /viewdatabase`

Returns saved analysis results from the SQLite database.

FastAPI automatically generates interactive API documentation. When the server is running locally, it can be accessed at:

```text
http://127.0.0.1:8000/docs
```

## Example API Input

A request to `/analyse` follows the structure:

```json
{
  "company": "Example Company",
  "role": "Software Engineer",
  "job_description": "Looking for a developer with Python and SQL experience.",
  "candidate_profile": "Experience building Python applications and working with SQL databases."
}
```

The returned analysis contains the structured assessment, matched and missing skills, experience and education matches, and the calculated suitability score.

## Technology Stack

* **Python 3.14**
* **Pydantic** — data validation and structured models
* **OpenRouter** — LLM API access
* **OpenAI-compatible Python client** — communication with the LLM API
* **FastAPI** — HTTP API
* **Uvicorn** — local ASGI server
* **SQLite** — persistence
* **pytest** — automated testing
* **uv** — dependency and environment management
* **Git / GitHub** — version control

## Project Structure

```text
2nd_DA_project/
│
├── src/
│   └── job_application_analysis/
│       ├── api.py
│       ├── choice.py
│       ├── main.py
│       ├── models.py
│       ├── OpRo_ai_client.py
│       ├── ai_client.py
│       ├── output.py
│       ├── scoring.py
│       ├── sql_database.py
│       └── user_input_func.py
│
├── tests/
│   ├── test_choice.py
│   ├── test_score.py
│   └── test_user_input_func.py
│
├── job_app_db.db
├── pyproject.toml
└── uv.lock
```

## Running Locally

This project uses `uv` for dependency and environment management.

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure the API key

The active AI client loads its API key from a local `.env` file using `python-dotenv`.

The environment variable expected by the active client is:

```text
OPRO_API_KEY
```

For example:

```text
OPRO_API_KEY=your_api_key_here
```

Do not commit your `.env` file or API key to GitHub.

### 3. Run the CLI application

```bash
uv run python -m job_application_analysis.main
```

### 4. Run the FastAPI application

```bash
uv run uvicorn job_application_analysis.api:fastapi_obj --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Engineering Decisions

### Why use an LLM?

Traditional rule-based matching would require manually defining how different job descriptions and candidate profiles should be interpreted.

The LLM provides flexible natural-language analysis, such as identifying requirements and comparing them with a candidate profile.

However, the project does not rely on the LLM for every decision.

### Why not let the LLM generate the final score?

LLM output is probabilistic.

A numerical score used for decision-making should follow predictable rules. Therefore, the LLM produces the information needed for scoring, while Python applies the scoring rules.

This creates a separation between:

```text
AI reasoning
    ↓
structured data
    ↓
deterministic business logic
```

### Why use Pydantic?

The application needs predictable data structures at multiple stages.

Pydantic provides validation for both the incoming job application and the structured AI response, allowing later parts of the system to work with defined models rather than arbitrary dictionaries.

### Why use SQLite?

The project needed persistent storage without introducing the overhead of a larger database system.

SQLite provides a simple local relational database suitable for the scope of this application.

## Testing Approach

The tests focus on behaviour that is important to the application rather than testing every possible input combination.

For example, the test suite checks:

```text
calculate_score()
    ├── strong match
    ├── no skills match
    └── education-only match

choice()
    ├── no AI response
    └── successful AI response

user_input()
    ├── valid input
    └── empty input → retry → valid input
```

The user-input tests use pytest's `monkeypatch` fixture to replace the real CLI `input()` function with controlled test input. This allows the tests to run automatically without requiring manual terminal interaction.

## Current Limitations

This is a portfolio project rather than a production application.

The quality of the analysis depends partly on the LLM's ability to correctly identify job requirements and compare them with the candidate profile.

The current scoring system also depends on the quality of the structured requirements and matches produced by the model.

The project does not currently include production concerns such as authentication, deployment infrastructure, or a production database.

## Future Improvements

Possible future improvements include:

* Expanding automated test coverage
* Improving separation between API logic and CLI display logic
* Making database initialisation automatic for a fresh installation
* Improving configuration and deployment support
* Adding a user interface on top of the existing API
* Improving the robustness of the AI analysis and validation process

## What I Learned

This project brought together several areas of software development in one system:

* Structuring a Python project into modules
* Working with external APIs
* Sending and receiving structured JSON
* Validating data with Pydantic
* Integrating an LLM into an application
* Separating AI behaviour from deterministic business logic
* Designing a SQLite persistence layer
* Building HTTP endpoints with FastAPI
* Handling errors across different parts of an application
* Writing automated tests with pytest
* Using Git and GitHub throughout development

The main goal was not simply to build an AI application, but to understand how an AI component can be incorporated into a broader software-engineering system.
