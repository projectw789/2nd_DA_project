def calculate_score(key_requirements, matched_skills, experience_match, education_match ):
    if key_requirements == []:
        score_1 = 0
        print("no key requirements")

    else:
        if len(matched_skills )== 0:
            print("Candidate does not have any of the required skills")
            score_1 = 0
        elif len(matched_skills) <= len(key_requirements):
            score_1 = len(matched_skills)/len(key_requirements) * 50
        else:
            score_1 = 50

    if experience_match == True:
        score_2 = 30
    else:
        score_2 = 0
        print("no experience match")

    if education_match == True:
        score_3 = 20
    else:
        score_3 = 0
        print("no education match")

    total_score = score_1 + score_2 + score_3
    t_score = int(total_score)
    return t_score