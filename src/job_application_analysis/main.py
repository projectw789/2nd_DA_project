from .user_input_func import user_input
from .ai_client import call_mistral
from .models import JobApplication, MistralOutput
from .scoring import calculate_score


user_app_obj = user_input()



ai_response = call_mistral(user_app_obj)

if ai_response == None:
    print("sorry")
else:
    print(ai_response)

suitability_score = calculate_score(ai_response.key_requirements, ai_response.matched_skills, ai_response.experience_match, ai_response.education_match)

print(suitability_score)


# uv run python -m job_application_analysis.main


  