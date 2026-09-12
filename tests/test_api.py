from fastapi.testclient import TestClient
from job_application_analysis.api import fastapi_obj
from job_application_analysis.models import OpRoOutput


def test_api_view_db_success():
    view_db_test_client = TestClient(fastapi_obj)
    response = view_db_test_client.get("/viewdatabase")
    assert response.status_code == 200

def test_api_view_db_fail(monkeypatch):
    def fail_view_db():
        return False
    monkeypatch.setattr("job_application_analysis.api.show_results_api_ver", fail_view_db)
    view_db_test_client = TestClient(fastapi_obj)
    response = view_db_test_client.get("/viewdatabase")
    assert response.status_code == 500


def test_api_analyse_LLM_fail(monkeypatch):
    def ai_fail(_):
        return None
    monkeypatch.setattr("job_application_analysis.api.call_opro_client", ai_fail)
    ai_output_test_client = TestClient(fastapi_obj)
    response = ai_output_test_client.post("/analyse", json = {
        "company" : "test",
        "role" : "test",
        "job_description" : "test",
        "candidate_profile" : "test"
    })
    assert response.status_code == 500

def test_api_analyse_LLM_success(monkeypatch):
    def false_llm_success(_):
        fake_output_dict = {
            "key_requirements" : ["1","2"],
            "matched_skills" : ["1","2"],
            "missing_skills" : [],
            "education_match" : True,
            "experience_match" : True,
            "assessment" : "a",
            "reasoning" : "a"
        }
        fake_output_obj = OpRoOutput(**fake_output_dict)
        return fake_output_obj

    def fake_save_analysis(_ , __):
        return "Analysis and input saved to database"
           
    monkeypatch.setattr("job_application_analysis.api.call_opro_client", false_llm_success)
    monkeypatch.setattr("job_application_analysis.api.save_analysis", fake_save_analysis)

    test_client = TestClient(fastapi_obj)
    response = test_client.post("/analyse", json = {
        "company" : "test",
        "role" : "test",
        "job_description" : "test",
        "candidate_profile" : "test"
    })
    assert response.status_code == 200
