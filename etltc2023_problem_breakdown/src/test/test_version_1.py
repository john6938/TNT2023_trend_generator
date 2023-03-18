from main.version_1 import describe_difference


def test_describe_difference():
    assert describe_difference(1, 1) == "remain the same"
    assert describe_difference(1.8, 1.7) == "decrease"
    assert describe_difference(51.22, 51.23) == "increase"
