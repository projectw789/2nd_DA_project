from fastapi import FastAPI
from .models import JobApplication
from .OpRo_ai_client import call_opro_client
from .choice import choice
from .output import display_result
from .sql_database import save_analysis, show_results_api_ver


fastapi_obj = FastAPI()

@fastapi_obj.post("/analyse")
def analyse(user_app_input : JobApplication):
    ai_response = call_opro_client(user_app_input)

    if ai_response == None:
        response = {
            "analysis" : False,
            "database_save" : False,
            "error_message" : "ai failed and returned nothing, nothing could be saved to database"
        }
        return response

    final_output = choice(ai_response)
    display_result(final_output)
    saved_results = save_analysis(user_app_input, final_output)

    if saved_results == "Analysis and input not saved to database due to technical error.please try again later.":
        response = {
            "analysis" : final_output,
            "database_save" : False,
            "error_message" : "saving to database failed"
        }
        return response
    return final_output

    

@fastapi_obj.get("/viewdatabase")
def view_database():
    output = show_results_api_ver()

    if output == "Database not shown due to tehcnical errors. plase try again later":
        response = {
            "database_shown" : False,
            "error_message" : "database not shown due to sql errors"
        }
        return response  
    
    return output

    
    