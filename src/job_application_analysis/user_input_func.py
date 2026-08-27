def user_input():
    while True:
        company_input = input("What company?  ")
        role_input = input("What role? ")
        jobdesc_input = input("WHats the job description?  ")
        candidateprofile_input = input("whats your candidate profile?  ")

        if company_input == ("") or role_input == ("") or jobdesc_input == ("") or candidateprofile_input == ("") :
            print("none of the inputs can be empty")
            

        else:
            break

    job_application = {
    "company" : company_input,
    "role" : role_input,
    "job description" : jobdesc_input,
    "candidate profile" : candidateprofile_input 
}

    return job_application