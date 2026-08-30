from pydantic import BaseModel

# uv run python -m job_application_analysis.models

class JobApplication(BaseModel):
    company : str
    role : str
    job_description : str
    candidate_profile : str
    

class MistralOutput(BaseModel):
    suitability_score : int
    key_requirements : list[str]
    matched_skills : list[str]
    missing_skills : list[str]
    experience_gap : str
    education_match : bool
    assessment : str
    reasoning : str

