from dotenv import load_dotenv
from openai import OpenAI
import os
import json
from .models import OpRoOutput
from pydantic import ValidationError


load_dotenv()

api_key = os.getenv("OPRO_API_KEY")

opro_client = OpenAI(api_key=api_key, base_url = "https://openrouter.ai/api/v1")

def call_opro_client(job_application):
    for attempt in range (3):
        try:
            response_object = opro_client.chat.completions.create(
                model="openrouter/free", 
                response_format = {"type":"json_object"}, 
                messages = [
                    { 
                        "role": "user",
                        "content": f"""
                        Analyse the following job application.

                        Identify:
                        - key skills and requirements in the job description
                        - skills and relevant experience shown in the candidate profile
                        - strong matches
                        - important gaps
                        - overall suitability
                        - your reasoning

                        Your response must contain exactly these 7 fields:

                        key_requirements (list of strings)
                        matched_skills (list of strings)
                        missing_skills (list of strings)
                        experience_match (boolean)
                        education_match (boolean)
                        assessment (string)
                        reasoning (string)

                        Do not include suitability_score or any additional fields.

                        Ensure the number of matched skills does not exceed the total number of key requirements.

                        Job application data:
                        {job_application}
                        """ 
                    }
                ]
            )
            dictio = json.loads(response_object.choices[0].message.content)
            valid_obj = OpRoOutput(**dictio)
            return valid_obj

        except ValidationError as e:
            print(e)
            continue
        except json.JSONDecodeError as e:
            print(e)
            continue
        except Exception as e:
            print(e)
            continue
    print("sorry ai issues, try again later")
    return None
