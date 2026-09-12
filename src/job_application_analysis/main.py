from .user_input_func import user_input
from .OpRo_ai_client import call_opro_client
from .output import display_result
from .sql_database import save_analysis, show_results, database_setup
from .choice import choice


def main():
    user_app_obj = user_input()


    ai_response = call_opro_client(user_app_obj)



    final_output = choice(ai_response)

    database_setup()

    display_result(final_output)

    save_analysis(user_app_obj, final_output)

    print("")
    print("")

    results = show_results(final_output)
    print(results)

if __name__ == "__main__":
    main()


# uv run python -m job_application_analysis.main


  