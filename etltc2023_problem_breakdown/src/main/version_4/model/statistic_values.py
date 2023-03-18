from __future__ import annotations
from current_discription_object import CurrentDescriptionObject
from verb_group import VerbGroup
from verb_groups import VerbGroups


class StatisticValues:
    __statistic_values: list[float]

    def __init__(self, statistic_values: list[float]) -> None:
        self.__statistic_values = statistic_values

    def add(self, statistic_value: float) -> StatisticValues:
        return StatisticValues([self.__statistic_values, statistic_value])

    def add_all(self, statistic_values: list[float]) -> StatisticValues:
        return StatisticValues(self.__statistic_values + statistic_values)

    def generate_descriptive_verb(
        self, current_description_object: CurrentDescriptionObject
    ) -> str:
        # TODO このメソッドを完成させる。
        current_index: int = current_description_object.get_target_index()
        if current_index == 0:
            return "is"

        current_value: float = self.__statistic_values[current_index]

        verb_group: VerbGroup = VerbGroups.get_verb_group(current_description_object)
        if current_index - 2 < 0:
            return verb_group.describe_difference()
