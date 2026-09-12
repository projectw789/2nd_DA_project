# AI-Powered Job Application Intelligence & Automation System

My application is designed to accept information from a user (including company, role, job description and the user's/candidate's portfolio/credentials) to assess a candidate's suitability to a job occupation.


## Functionality

 Inputs are recieved from a user in string format. Pydantic which validates and structures inputs and outputs. Upon validation, input is passed through to an LLM where the canididates suitability is assessed and scored. The LLM output is also validated via pydantic and a score is calculated and produced by python based on the LLM's output. Then a final object including the score and LLM output is created. If a database doesn't exist already, then it is created. The object gets saved to the database organised in columns. The database code is coded via sqlite. The user can also decide to view the database of saved applications. API integration is included so this application can run via the CLI or API. There is extensive error handling for common and predictable errors. Pytests used to test functions (e.g api, score etc.) to ensure clean functionality.

 ## Features

Pydantic
Error Handling
LLM integration
Scoring
SQLite
FastAPI
Testing (via pytest)

## Workflow

1) CLI/HTTP API
2) User Input
3) Pydantic Validation
4) Data sent to LLM API
5) LLM output validation
6) Python Scoring
7) Structured final output object
8) SQLite database
9) FastAPI/CLI output

## How to run

- get api key
- .env set up
- uv set up
- download required packages
- can use CLI command or uvicorn command (then run code via api at website)

## Engineering decisions

- Pydantic = input, intermediary and output validation against structured layout
- LLM = artifical intelligence assessment of candidates' job suitability
- Python Scoring = Repeatable and quantitative scoring evaluation rather than unpredictable and non-repeatable qualitative scoring evaluations via LLM.
- SQLite = persistent local data storage for job analyses
- FastAPI = allows application functionality through HTTP API
- pytest = automated verification and testing of individual functions and components
- error handling = handling predictable and common errors smoothly

## Limitations

This currently is not integrated to an actualy UI friendly website and has to be run via CLI or starting server via CLI and then using the docs website. This also doesn't currently send analysis or database to an email or website or anything online, and the database currently lives within files of the users computer.

## Potential Improvements

Include sending of analyses to emails and websites, clean front end and hosted database for verified users.

## Learning

I was learning throughout the entire development of this application. Project developed in a way that I learned a new concept --> implemented --> tested --> saw what went wrong and why --> reimplemented with improvements --> repeated until code correct and running. That includes classes, error handling, apis, testing, LLM usage, .env usage, sql and more. I have learnt a lot and will be continuing to be programming and learning more code and making more applications and software.

