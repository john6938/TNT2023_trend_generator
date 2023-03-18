VERB_GROUPS: tuple = (
    ("increase", "remain the same", "decrease"),
    ("rise", "stay the same", "fall"),
)


def describe_difference(num_before: int, num_after: int, verb_group_id: int) -> str:
    description: str = ""
    if num_after > num_before:
        description = VERB_GROUPS[verb_group_id % VERB_GROUPS.len()][0]
    elif num_after == num_before:
        description = VERB_GROUPS[verb_group_id % VERB_GROUPS.len()][1]
    else:
        description = VERB_GROUPS[verb_group_id % VERB_GROUPS.len()][2]

    verb_group_id += 1
    return description
