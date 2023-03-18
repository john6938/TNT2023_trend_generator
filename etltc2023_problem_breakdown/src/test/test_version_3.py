from main.version_3 import check_and_append_verb, describe_difference, reinitialize_group_id
import main.version_3 as v3
from pytest_mock.plugin import MockerFixture
from unittest.mock import MagicMock


def test_describe_difference() -> None:
    assert describe_difference(5.822, 6.304, 2) == v3.VERB_GROUPS[2][0]
    assert describe_difference(942.109342, 942.109342, 4) == v3.VERB_GROUPS[0][1]
    assert describe_difference(-394205, -904020, 0) == v3.VERB_GROUPS[0][2]


def test_reinitialize_group_id() -> None:
    assert reinitialize_group_id(0, v3.VERB_GROUPS) == 1
    assert reinitialize_group_id(3, v3.VERB_GROUPS) == 0
    assert reinitialize_group_id(4, v3.VERB_GROUPS) == 1
    assert reinitialize_group_id(104205, v3.VERB_GROUPS) == 2


def test_check_and_append_verb_case_changes_are_different_direction(
    mocker: MockerFixture,
) -> None:
    num_before: float = 0.0
    num_after: float = 1.0
    difference_before: int = 0
    difference_after: int = 1
    verb_group_id: int = 2

    return_description: str = "hello"
    return_group_id: int = 100

    describe_difference_mock: MagicMock = mocker.patch(
        "main.version_3.describe_difference", return_value=return_description
    )
    reinitialize_group_id_mock: MagicMock = mocker.patch(
        "main.version_3.reinitialize_group_id", return_value=return_group_id
    )

    result1, result2 = check_and_append_verb(
        num_before, num_after, difference_before, difference_after, verb_group_id
    )

    describe_difference_mock.assert_called_with(num_before, num_after, verb_group_id)
    reinitialize_group_id_mock.assert_called_with(verb_group_id, v3.VERB_GROUPS)
    assert result1 == return_description
    assert result2 == return_group_id


def test_check_and_append_verb_case_changes_are_same_direction(
    mocker: MockerFixture,
) -> None:
    num_before: float = 0.0
    num_after: float = 1.0
    difference: int = 1
    verb_group_id: int = 2

    return_description: str = "hello"
    return_group_id: int = 100

    describe_difference_mock: MagicMock = mocker.patch(
        "main.version_3.describe_difference", return_value=return_description
    )
    reinitialize_group_id_mock: MagicMock = mocker.patch(
        "main.version_3.reinitialize_group_id", return_value=return_group_id
    )

    result1, result2 = check_and_append_verb(
        num_before, num_after, difference, difference, verb_group_id
    )

    reinitialize_group_id_mock.assert_called_with(verb_group_id, v3.VERB_GROUPS)
    describe_difference_mock.assert_called_with(num_before, num_after, return_group_id)
    assert result1 == return_description
    assert result2 == return_group_id
