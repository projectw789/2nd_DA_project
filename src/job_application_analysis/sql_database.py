import sqlite3
import json

def database_setup():
    for attempt in range(3):
        sql_connect, cursor = (None, None)
        try:
            sql_connect = sqlite3.Connection("job_app_db.db")
            cursor = sql_connect.cursor()
            cursor.execute(" CREATE TABLE IF NOT EXISTS database( ID INTEGER PRIMARY KEY, COMPANY TEXT, ROLE TEXT, SUITABILITY_SCORE INT, KEY_REQUIREMENTS TEXT, MATCHED_SKILLS TEXT, MISSING_SKILLS TEXT, EXPERIENCE_MATCH INT, EDUCATION_MATCH INT, ASSESSMENT TEXT, REASONING TEXT )")
            sql_connect.commit()
            
            return "database succesfully created"
        except sqlite3.Error as e:
            print(e)
            continue
        finally:
            if sql_connect is not None:
                sql_connect.close()

    raise sqlite3.Error("experiencing unexpected sql errors. apologies")


def fresh_sql_connect():

    sql_connect = sqlite3.Connection("job_app_db.db")
    cursor = sql_connect.cursor()
    return sql_connect, cursor

    

    


def save_analysis(job_application, final_output):

    if final_output == "sorry":
        return ("Database not created.")
    else:
        for attempt in range(3):
            sql_connect, cursor = (None, None)
            try:
                sql_connect, cursor = fresh_sql_connect()
                key_req_str = json.dumps(final_output.key_requirements)
                ma_sk_str = json.dumps(final_output.matched_skills)
                mi_sk_str = json.dumps(final_output.missing_skills)
                cursor.execute("INSERT INTO database (COMPANY, ROLE, SUITABILITY_SCORE, KEY_REQUIREMENTS, MATCHED_SKILLS, MISSING_SKILLS, EXPERIENCE_MATCH, EDUCATION_MATCH, ASSESSMENT, REASONING) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (job_application.company, job_application.role, final_output.suitability_score, key_req_str, ma_sk_str, mi_sk_str, final_output.experience_match, final_output.education_match, final_output.assessment, final_output.reasoning))
                sql_connect.commit()
                
                return "Analysis and input saved to database"
            except sqlite3.Error as e:
                print(e)
                continue
            finally:
                if sql_connect is not None:
                    sql_connect.close()
        print("Analysis and input not saved to database due to technical error.please try again later.")
        save_fail = False
        return save_fail
        

def show_results(final_output):
    if final_output == "sorry":
        return ("Database not shown due to AI tehcnical issues.")
    else:
        for attempt in range(2):
            user_choice = input("Would you like to view the database of results? (Answer as Yes or No) ")
            print("")
            print("")
            sql_connect, cursor = (None, None)
            try:
                sql_connect, cursor = fresh_sql_connect()
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

            finally:
                if sql_connect is not None:
                    sql_connect.close()
                
        return "Database not shown due to tehcnical errors. plase try again later"



def show_results_api_ver():

    for attempt in range(2):
        api_dict = {}
        i = 0
        sql_connect, cursor = (None, None)
        try:
            sql_connect, cursor = fresh_sql_connect()
                
            cursor.execute("SELECT * FROM database") 
            whole_database = cursor.fetchall() 
            for row in whole_database:
                api_dict[f"entry no.{i}"] = {}
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
                api_dict[f"entry no.{i}"]["ID"] = row[0]
                api_dict[f"entry no.{i}"]["Company"] = row[1]
                api_dict[f"entry no.{i}"]["Role"] = row[2]
                api_dict[f"entry no.{i}"]["Suitability Score"] = row[3]
                api_dict[f"entry no.{i}"]["Key Requirements"] = python_key_req
                api_dict[f"entry no.{i}"]["Matched Skills"] = python_ma_sk
                api_dict[f"entry no.{i}"]["Missing Skills"] = python_mi_sk
                api_dict[f"entry no.{i}"]["Experience Match"] = python_ex_ma
                api_dict[f"entry no.{i}"]["Education Match"] = python_ed_ma
                api_dict[f"entry no.{i}"]["Assessment"] = row[9]
                api_dict[f"entry no.{i}"]["Reasoning"] = row[10]
                i = i+1
            return api_dict             
                   
        except sqlite3.Error as e:
            print(e)
            continue

        except Exception as e:
            print(e)
            continue

        finally:
            if sql_connect is not None:
                sql_connect.close()
                
    return False


# uv run python -m job_application_analysis.sql_database