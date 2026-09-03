def display_result(final_output):
    if final_output == "sorry":
        return ("Results not shown.")
    else:
        print("")
        print("")
        print("")

        print("JOB APPLICATION ANALYSIS")
        print("")
        print(f"SUITABILITY SCORE: {final_output.suitability_score}/100")
        print("")
        print("")
        print(" JOB REQUIREMENTS:")
        print("")
        for requirement in final_output.key_requirements:
            print(f"- {requirement}")
        print("")
        print("")
        print("MATCHED SKILLS:")
        print("")
        if len(final_output.matched_skills) == 0:
            print("No matched skills.")
        else:
            for skill in final_output.matched_skills:
                print(f"- {skill}")
        print("")
        print("")
        print("MISSING SKILLS:")
        print("")
        if len(final_output.missing_skills) == 0:
            print("No missing skills.")
        else:
            for skill in final_output.missing_skills:
                print(f"- {skill}")

        print("")
        print("")

        if final_output.experience_match:
            print("EXPERIENCE MATCH : YES")
        else:
            print("EXPERIENCE MATCH : NO")

        if final_output.education_match:
            print("EDUCATION MATCH : YES")
        else:
            print("EDUCATION MATCH: NO")

        print("")
        print("")

        print((final_output.assessment))
        print("")
        print("")
        print((final_output.reasoning))

    