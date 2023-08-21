from collections.abc import Sized

VERB_GROUPS: tuple = (
    ("increase", "remain the same", "decrease"),
    ("rise", "stay the same", "fall"),
    ("go up", "stay flat", "go down"),
    ("grow", "remain unchanged", "shrink"),
)


def describe_difference(num_before: float, num_after: float, verb_group_id: int) -> str:
    """
    Describe the difference between two numbers.
    Arguments:
        num_before: The first number.
        num_after: The second number.
        verb_group_id: The group of verbs to use.
    Returns:
        A string describing the difference between the two numbers.
    """
    if num_after > num_before:
        return VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][0]
    if num_after == num_before:
        return VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][1]

    return VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][2]


def reinitialize_group_id(group_id: int, group: Sized) -> int:
    """Reinitialize the group id.

    Args:
        group_id (int): the id of the group.
        group (Sized): the group.

    Returns:
        int: the new group id.
    """
    return (group_id + 1) % len(group)


def check_and_append_verb(
    num_before: float,
    num_after: float,
    difference_before: int,
    difference_after: int,
    verb_group_id: int,
) -> tuple[str, int]:
    """
    Checks to see if the difference between two numbers has changed, and appends a verb to the
    description of the difference if it has. Also increments the verb group ID if the difference
    has changed.

    Args:
        num_before (float): the number before the operation
        num_after (float): the number after the operation
        difference_before (int): the difference between the two numbers before the operation
        difference_after (int): the difference between the two numbers after the operation
        verb_group_id (int): the ID of the group of verbs that can be used to describe the
            difference

    Returns:
        tuple[str, int]: the description of the difference, and the new verb group ID
    """
    if difference_before == difference_after:
        new_verb_group_id = reinitialize_group_id(verb_group_id, VERB_GROUPS)
        return (describe_difference(num_before, num_after, new_verb_group_id), new_verb_group_id)

    return (
        describe_difference(num_before, num_after, verb_group_id),
        reinitialize_group_id(verb_group_id, VERB_GROUPS),
    )
    