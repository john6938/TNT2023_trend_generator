class CurrentDescriptionObject:
    __target_index: int
    __verb_group_id: int

    def __init__(self, target_index: int, verb_group_id: int) -> None:
        self.__target_index = target_index
        self.__verb_group_id = verb_group_id

    def get_target_index(self) -> int:
        return self.__target_index

    def get_verb_gropu_id(self) -> int:
        return self.__verb_group_id
