
import builtins
from job_application_analysis.user_input_func import user_input
from job_application_analysis.models import JobApplication

def test_user_input_no_loop(monkeypatch):
    test_input_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    iterative_list = iter(test_input_list)
    
    def list_iteration(placeholder):     
        return next(iterative_list)
    monkeypatch.setattr(builtins, "input", list_iteration)
    obj = user_input()
    assert isinstance(obj, JobApplication)

def test_user_input_one_loop(monkeypatch):
    test_input_list = ["", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    iterative_list = iter(test_input_list)
    
    def list_iteration(placeholder):      
        return next(iterative_list)
    monkeypatch.setattr(builtins, "input", list_iteration)
    obj = user_input()
    assert isinstance(obj, JobApplication)
    