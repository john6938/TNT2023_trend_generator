from __future__ import annotations
from value_change import ValueChange


class ChangeType:
    __change_type: int
    INCREASING: int = 0
    FLAT: int = 1
    DECREASING: int = 2
    UNDEFINED: int = -1

    def __init__(self, change_type: int) -> None:
        self.__change_type = change_type

    def get_change_type(self) -> int:
        return self.__change_type

    def check_change_type(self, value_change: ValueChange) -> ChangeType:
        num_before, num_after = value_change.get_value_change()

        if num_after > num_before:
            return ChangeType(self.INCREASING)
        if num_after == num_before:
            return ChangeType(self.FLAT)
        return ChangeType(self.DECREASING)
