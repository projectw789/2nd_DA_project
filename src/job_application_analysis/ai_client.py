from dotenv import load_dotenv
from mistralai.client import Mistral
from mistralai.client.errors import SDKError
import os
import json
from .models import MistralOutput
from pydantic import ValidationError


load_dotenv()

api_key = os.getenv("MISTRALAI_API_KEY")

mistral_client = Mistral(api_key = api_key)

# uv run python -m job_application_analysis.ai_client
def call_mistral(job_application):
    for attempt in range(3):
        try:
            response = mistral_client.chat.complete(
                model = "mistral-small-latest",
                response_format= {"type": "json_object"},
                messages = [
                    {
                        "role" : "user",
                        "content" : f"Analyse the following job application. Identify the key skills and requirements in the job description, the skills and relevant experience shown in the candidate profile, strong matches, important gaps, overall suitability, and your reasoning. Your response must contain exactly these 7 fields: key_requirements (list of strings), matched_skills (list of strings), missing_skills (list of strings), experience_match (boolean), education_match (boolean), assessment (string), reasoning (string). Do not include suitability_score or any additional fields. Ensure the number of matched skills do not exceed the total number of key requirements. Job application data: {job_application}"
                    }
                ]
            )
            dictio = json.loads(response.choices[0].message.content)
            valid_obj = MistralOutput(**dictio)
            return valid_obj

        except ValidationError as e:
            print(e)
            continue
        except json.JSONDecodeError as e:
            print(e)
            continue
        except SDKError as e:
            print(e)
            continue
        except Exception as e:
            print(e)
            continue
    print("sorry ai issues, try again later")
    return None
