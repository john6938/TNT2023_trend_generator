from app.task4 import describe_difference, check_and_append_verb


def test_describe_difference():
    assert describe_difference(1, 1, 2) == "remain flat"
    assert describe_difference(1.8, 1.7, 0) == "decrease"

def test_check_and_append_verb():
    assert check_and_append_verb(2.5, 1.4, 1, 2, 2) == 