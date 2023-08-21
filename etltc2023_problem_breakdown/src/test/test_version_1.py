from main.version_1 import describe_difference


def test_describe_difference() -> None:
    assert describe_difference(1, 1) == "remain the same"
    assert describe_difference(8, 7) == "decrease"
    assert describe_difference(5122, 5123) == "increase"
