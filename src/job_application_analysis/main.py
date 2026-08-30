from .user_input_func import user_input
from .ai_client import call_mistral
from .models import JobApplication



user_app_dict = user_input()

user_object = JobApplication(**user_app_dict)


ai_response = call_mistral(user_object)

print(ai_response)

# uv run python -m job_application_analysis.main


  