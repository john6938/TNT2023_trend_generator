VERB_GROUPS: tuple = (
    ("increase", "remain the same", "decrease"),
    ("rise", "stay the same", "fall"),
)


def describe_difference(num_before: int, num_after: int, verb_group_id: int) -> tuple[str, int]:
    description: str = ""
    if num_after > num_before:
        description = VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][0]
    elif num_after == num_before:
        description = VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][1]
    else:
        description = VERB_GROUPS[verb_group_id % len(VERB_GROUPS)][2]

    verb_group_id += 1
    return description, verb_group_id
