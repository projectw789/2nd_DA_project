from fastapi import FastAPI
from .models import JobApplication
from .OpRo_ai_client import call_opro_client
from .choice import choice
from .output import display_result
from .sql_database import save_analysis


fastapi_obj = FastAPI()

@fastapi_obj.post("/analyse")
def analyse(user_app_input : JobApplication):
    ai_response = call_opro_client(user_app_input)
    final_output = choice(ai_response)
    display_result(final_output)
    save_analysis(user_app_input, final_output)

    
    