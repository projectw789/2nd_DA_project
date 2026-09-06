import sqlite3
import json

sql_connect = sqlite3.Connection("job_app_db.db")

cursor = sql_connect.cursor()

cursor.execute(" CREATE TABLE IF NOT EXISTS database( ID INTEGER PRIMARY KEY, COMPANY TEXT, ROLE TEXT, SUITABILITY_SCORE INT, KEY_REQUIREMENTS TEXT, MATCHED_SKILLS TEXT, MISSING_SKILLS TEXT, EXPERIENCE_MATCH INT, EDUCATION_MATCH INT, ASSESSMENT TEXT, REASONING TEXT )")

sql_connect.commit()


def save_analysis(job_application, final_output):
    if final_output == "sorry":
        return ("Database not created.")
    else:
        key_req_str = json.dumps(final_output.key_requirements)
        ma_sk_str = json.dumps(final_output.matched_skills)
        mi_sk_str = json.dumps(final_output.missing_skills)
        cursor.execute("INSERT INTO database (COMPANY, ROLE, SUITABILITY_SCORE, KEY_REQUIREMENTS, MATCHED_SKILLS, MISSING_SKILLS, EXPERIENCE_MATCH, EDUCATION_MATCH, ASSESSMENT, REASONING) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (job_application.company, job_application.role, final_output.suitability_score, key_req_str, ma_sk_str, mi_sk_str, final_output.experience_match, final_output.education_match, final_output.assessment, final_output.reasoning))
        sql_connect.commit()

def show_results(final_output):
    if final_output == "sorry":
        return ("Database not shown due to AI tehcnical issues.")
    else:
        for attempt in range(2):
            user_choice = input("Would you like to view the database of results? (Answer as Yes or No) ")
            print("")
            print("")
            try:
                b_user_choice = user_choice.lower()
                if b_user_choice == "yes": 
                    cursor.execute("SELECT * FROM database") 
                    whole_database = cursor.fetchall() 
                    for row in whole_database:
                        try:
                            python_key_req = json.loads(row[4])   
                            python_ma_sk = json.loads(row[5])   
                            python_mi_sk = json.loads(row[6])
                        except json.JSONDecodeError:
                            python_key_req = "key req data error"
                            python_ma_sk = "matched skills data error"
                            python_mi_sk = "missing skills data error"
                        except TypeError:
                            python_key_req = "key req data error"
                            python_ma_sk = "matched skills data error"
                            python_mi_sk = "missing skills data error"
                        python_ex_ma = bool(row[7])
                        python_ed_ma = bool(row[8])
                        print(f"ID: {row[0]} \nCompany: {row[1]} \nRole: {row[2]} \nSuitability Score: {row[3]} \nKey Requirements: {python_key_req} \nMatched Skills: {python_ma_sk} \nMissing Skills: {python_mi_sk} \nExperience Match : {python_ex_ma} \nEducation Match: {python_ed_ma} \nAssessment: {row[9]} \nReasoning: {row[10]}")
                        print("")
                        print("")
                    return ("")

                elif b_user_choice == "no":
                    return ("Database not shown.")

                elif attempt != 1:
                    print("Incorrect input.")
                    continue

                elif attempt == 1:
                    return ("Database not shown.")
                
            except sqlite3.Error:
                print("Facing technical issues. Restart the program.")
                return ("Technical issues, please try again later.")
                





# uv run python -m job_application_analysis.sql_database