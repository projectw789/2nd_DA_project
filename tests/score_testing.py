from ..src.job_application_analysis.scoring import calculate_score

score = calculate_score (2,2,True,False)
assert score == 80



# uv run pytest tests/score_testing.py