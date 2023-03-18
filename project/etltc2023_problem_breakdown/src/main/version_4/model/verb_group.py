from change_type import ChangeType


class VerbGroup:
    __verb_group: dict

    def __init__(
        self, increasing_word: str, remaining_word: str, decreasing_word: str
    ) -> None:
        self.__verb_group[ChangeType.INCREASING] = increasing_word
        self.__verb_group[ChangeType.FLAT] = remaining_word
        self.__verb_group[ChangeType.DECREASING] = decreasing_word

    def describe_difference(self, change_type: ChangeType) -> str:
        return self.__verb_group[change_type.get_change_type()]
