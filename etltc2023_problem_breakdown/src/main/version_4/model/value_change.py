class ValueChange:
    __num_before: float
    __num_after: float

    def __init__(self, num_before: float, num_after: float) -> None:
        self.__num_before = num_before
        self.__num_after = num_after

    def get_value_change(self) -> tuple:
        return (self.__num_before, self.__num_after)
