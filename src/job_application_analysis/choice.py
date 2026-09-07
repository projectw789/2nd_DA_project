from .models import FinalOutput
from .scoring import calculate_score

def choice(ai_response):
    if ai_response is None:
        final_output = ("sorry")
        return final_output
    else:
        suitability_score = calculate_score(ai_response.key_requirements, ai_response.matched_skills, ai_response.experience_match, ai_response.education_match)
        final_output = FinalOutput(**ai_response.model_dump(),suitability_score=suitability_score)
        return final_output
