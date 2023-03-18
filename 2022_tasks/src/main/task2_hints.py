# function hints
def print_difference(data_1: list, data_2: list, rel: str, dif: float) -> None:
    """データの差分を出力する。

    Args:
        data_1 (list): データ１
        data_2 (list): データ２
        rel (str): 数値の変化に応じた動詞
        dif (float): 数値の変化の絶対値
    """

    print(
        f"The number of students {rel} from {data_1[1]} in {data_1[0]} by {dif} to {data_2[1]} in {data_2[0]}."
    )


def print_if_same(data_1: list, data_2: list, rel: str) -> None:
    """数値が同一の場合の出力をする。

    Args:
        data_1 (list): データ１
        data_2 (list): データ２
        rel (str): 数値の変化に応じた動詞
    """

    print(f"The number of students {rel} at {data_1[1]} from {data_1[0]} to {data_2[0]}.")


def compare_data(data_1: list, data_2: list) -> None:
    """２つのデータの差分に応じて出力をする。

    Args:
        data_1 (list): データ１
        data_2 (list): データ２
    """

    change = data_2[1] - data_1[1]
    rel = get_rel(change)
    if data_1[1] == data_2[1]:
        print_if_same(data_1, data_2, rel)
    else:
        dif = abs(change)
        print_difference(data_1, data_2, rel, dif)


# list hints
data_set = [["Mar", 25], ["Apr", 50], ["May", 50], ["Jun", 40], ["Jul", 60]]
"""データセット"""
