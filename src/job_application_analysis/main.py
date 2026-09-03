from .user_input_func import user_input
from .ai_client import call_mistral
from .models import FinalOutput
from .scoring import calculate_score
from .output import display_result
from .sql_database import save_analysis, show_results


user_app_obj = user_input()

ai_response = call_mistral(user_app_obj)

if ai_response is None:
    final_output = ("sorry")
else:
    suitability_score = calculate_score(ai_response.key_requirements, ai_response.matched_skills, ai_response.experience_match, ai_response.education_match)
    final_output = FinalOutput(**ai_response.model_dump(),suitability_score=suitability_score)

display_result(final_output)

save_analysis(user_app_obj, final_output)

print("")
print("")

results = show_results(final_output)
print(results)


# uv run python -m job_application_analysis.main


  