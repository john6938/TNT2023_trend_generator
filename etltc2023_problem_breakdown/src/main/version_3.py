from collections.abc import Sized

VERB_GROUPS: tuple = (
    ("increase", "remain the same", "decrease"),
    ("rise", "stay the same", "fall"),
    ("go up", "stay flat", "go down"),
    ("grow", "remain unchanged", "shrink"),
)


def describe_difference(num_before: float, num_after: float, verb_group_id: int) -> str:
    if num_after > num_before:
        return VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][0]
    if num_after == num_before:
        return VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][1]

    return VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][2]


def reinitialize_group_id(group_id: int, group: Sized) -> int:
    return group_id + 1 % len(group)


def check_and_append_verb(
    num_before: float,
    num_after: float,
    difference_before: int,
    difference_after: int,
    verb_group_id: int,
) -> tuple:
    if difference_before == difference_after:
        new_verb_group_id = reinitialize_group_id(verb_group_id, VERB_GROUPS)
        return describe_difference(num_before, num_after, new_verb_group_id), new_verb_group_id

    return (
        describe_difference(num_before, num_after, verb_group_id),
        reinitialize_group_id(verb_group_id, VERB_GROUPS),
    )
