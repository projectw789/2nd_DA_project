from pydantic import BaseModel, Field


# uv run python -m job_application_analysis.models

class JobApplication(BaseModel):
    company : str
    role : str
    job_description : str
    candidate_profile : str
    

class MistralOutput(BaseModel):
    
    key_requirements : list[str] = Field(min_length=1)
    matched_skills : list[str] 
    missing_skills : list[str] 
    experience_match : bool
    education_match : bool
    assessment : str = Field(min_length=1)
    reasoning : str = Field(min_length=1)

class FinalOutput(BaseModel):

    suitability_score : int
    key_requirements : list[str]
    matched_skills : list[str]
    missing_skills : list[str]
    experience_match : bool
    education_match : bool
    assessment : str
    reasoning : str

