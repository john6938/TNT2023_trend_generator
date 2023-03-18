from verb_group import VerbGroup
from verb_groups import VerbGroups
from current_discription_object import CurrentDescriptionObject


class VerbGroups:
    __verb_groups: tuple

    def __init__(self, verb_groups: tuple) -> None:
        self.__verb_groups = verb_groups

    def add(self, verb_group: VerbGroup) -> VerbGroups:
        return VerbGroups(tuple([self.__verb_groups, verb_group]))

    def get_verb_group(
        self, current_description_object: CurrentDescriptionObject
    ) -> VerbGroup:
        return self.__verb_groups[current_description_object.get_verb_gropu_id()]
