from dotenv import load_dotenv
from mistralai.client import Mistral
import os

load_dotenv()

api_key = os.getenv("MISTRALAI_API_KEY")

mistral_client = Mistral(api_key = api_key)

# uv run python -m job_application_analysis.ai_client
def call_mistral(job_application):
    
    response = mistral_client.chat.complete(
        model = "mistral-small-latest",
        messages = [
            {
                "role" : "user",
                "content" : f"Analyse the following job application. 1. Identify the key skills and requirements in the job description. 2. Identify the skills and relevant experience shown in the candidate profile. 3. Compare the candidate against the job requirements. 4. Identify strong matches and important gaps. 5. Give an overall suitability assessment for the role. 6. Explain your reasoning clearly. Job application data:{job_application}"
            }
        ]
    )

    return response.choices[0].message.content
