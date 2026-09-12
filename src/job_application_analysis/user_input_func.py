from .models import JobApplication
from pydantic import ValidationError

def user_input():
    while True:
        company_input = input("What company?  ")
        role_input = input("What role? ")
        jobdesc_input = input("Whats the job description?  ")
        candidateprofile_input = input("whats your candidate profile?  ")

        if company_input == ("") or role_input == ("") or jobdesc_input == ("") or candidateprofile_input == ("") :
            print("none of the inputs can be empty")
            continue

        job_application = {
            "company" : company_input,
            "role" : role_input,
            "job_description" : jobdesc_input,
            "candidate_profile" : candidateprofile_input 
            }
            
        
        try:
            job_app_obj = JobApplication(**job_application)
            return job_app_obj
        except ValidationError:
            print("wrong input format")
            continue
