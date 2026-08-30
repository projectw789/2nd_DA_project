from dotenv import load_dotenv
from mistralai.client import Mistral
import os
import json


load_dotenv()

api_key = os.getenv("MISTRALAI_API_KEY")

mistral_client = Mistral(api_key = api_key)

# uv run python -m job_application_analysis.ai_client
def call_mistral(job_application):
    
    response = mistral_client.chat.complete(
        model = "mistral-small-latest",
        response_format= {"type": "json_object"},
        messages = [
            {
                "role" : "user",
                "content" : f"Analyse the following job application. Identify the key skills and requirements in the job description, the skills and relevant experience shown in the candidate profile, strong matches, important gaps, overall suitability, and your reasoning. Your response must contain exactly these 8 fields: suitability_score (integer from 0 to 100), key_requirements (list of strings), matched_skills (list of strings), missing_skills (list of strings), experience_gap (string), education_match (boolean), assessment (string), reasoning (string). Do not include any additional fields. Job application data: {job_application}"
            }
        ]
    )
    dictio = json.loads(response.choices[0].message.content)

    return dictio
