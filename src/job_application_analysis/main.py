from .user_input_func import user_input
from .ai_client import call_mistral

user_app_dict = user_input()

ai_response = call_mistral(user_app_dict)

print(ai_response)

# uv run python -m job_application_analysis.main 


  