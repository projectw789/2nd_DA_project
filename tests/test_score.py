from job_application_analysis.scoring import calculate_score


def test_score():
    score = calculate_score(["1","2"],["1","2"],True,False)
    assert score == 80


def test_score_two():
    score = calculate_score(["1","2"],[],False,False)
    assert score == 0


def test_score_three():
    score = calculate_score(["1","2"],["1","2"],False,True)
    assert score == 70

def test_scoe_four():
    score = calculate_score(["1","2"],["1","2","3"],False,True)
    assert score == 70

# uv run pytest tests/score_testing.py