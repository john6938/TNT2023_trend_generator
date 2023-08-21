from main.version_2 import describe_difference
import main.version_2 as v2


def test_describe_difference() -> None:
    verb_group_id = 0
    verb, verb_group_id = describe_difference(1, 2, verb_group_id)
    assert verb == v2.VERB_GROUPS[0][0]
    assert verb_group_id == 1
    verb, verb_group_id = describe_difference(4, 4, verb_group_id)
    assert verb == v2.VERB_GROUPS[1][1]
    assert verb_group_id == 2
    verb, verb_group_id = describe_difference(83, 39, verb_group_id)
    assert verb == v2.VERB_GROUPS[0][2]
    assert verb_group_id == 3
    verb, verb_group_id = describe_difference(204, 203, verb_group_id)
    assert verb == v2.VERB_GROUPS[1][2]
    assert verb_group_id == 4
