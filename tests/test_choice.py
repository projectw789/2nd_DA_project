from job_application_analysis.choice import choice
from job_application_analysis.models import OpRoOutput, FinalOutput


def test_choice_ai_error():
    final_output = choice(None)
    assert final_output == "sorry"


def test_choice_ai_success():
    mock_ai_output = {
        "key_requirements" : ["1","2"],
        "matched_skills" : ["1", "2"],
        "missing_skills" : [],
        "experience_match" : True,
        "education_match" : False,
        "assessment" : "string",
        "reasoning" : "string"
    }
    mock_ai_obj = OpRoOutput(**mock_ai_output)
    mock_final_obj = choice(mock_ai_obj)
    assert isinstance(mock_final_obj, FinalOutput)

