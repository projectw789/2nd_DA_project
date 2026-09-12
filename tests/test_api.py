from fastapi.testclient import TestClient
from job_application_analysis.api import fastapi_obj


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