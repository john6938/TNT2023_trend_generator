import datetime
import math

INFINITIVE_VERB: dict = {"go": "went", "do": "did", "have": "had"}
VERB_GROUP: dict


def connect_two_sentence(change1: str, change2: str) -> bool:
    """2つの文章を繋げるかどうかを判定する。
        Determine if the two sentences can be connected.

    Args:
        change1 (str): 1つ目の変動 First Change
        change2 (str): 2つ目の変動 Second Change

    Returns:
        bool: 1つ目と2つ目の変動が同じ場合True
            If two values are the same, return True.
    """
    if change1 == change2:
        return True
    else:
        return False


def append_min_max(number: float, sentence: str) -> str:
    """数値が最大または最小の時、文章を追加する。
        If the number is max or min, append strings to the sentence.

    Args:
        number (float): 数値 Number
        sentence (str): 文章 Sentence

    Returns:
        str: 変更後の文章 The modified sentence.
    """
    MAX = ["peaked", "hit a high"]
    MIN = ["hit a low"]

    max_num = 15.5
    min_num = 3.11
    if number == min_num:
        sentence += MIN[0]
    elif number == max_num:
        sentence += MAX[0]

    return sentence


def create_sentence(title: str, data: list) -> str:
    """新たに文章を作成する。

    Args:
        title (str): 主題
        data (list): グラフのデータ

    Returns:
        str: 作成された文章
    """
    sentence = ""
    sentence += title
    return f"{sentence} shows, {data}"


def append_verb(change1: int, change2: int, verb_group_id: int, sentnece: str) -> str:
    """文章に動詞を追加する。

    Args:
        change1 (int): 変動１
        change2 (int): 変動２
        verb_group_id (int): 動詞グループID
        sentnece (str): 文章

    Returns:
        str: 文章
    """
    if change1 == change2:
        verb_group_id += 1
        sentnece += VERB_GROUP[verb_group_id]
        return sentnece
    else:
        sentnece += VERB_GROUP[verb_group_id]
        verb_group_id += 1
        return sentnece


def summerize_sentence(max_num: float, min_num: float, start_num: float, end_num: float) -> str:
    """文章を要約する。

    Args:
        max_num (float): 最大値
        min_num (float): 最小値
        start_num (float): 開始値
        end_num (float): 終了値

    Returns:
        str: 要約
    """
    up_text: str
    down_text: str
    fluctuate_text: str
    flat_text: str

    if (end_num - start_num) > 20:
        return up_text
    elif (start_num - end_num) > 20:
        return down_text
    else:
        if (max_num - min_num) > 20:
            return fluctuate_text
        else:
            return flat_text


def show_change_strength(num1: float, num2: float) -> str:
    """変動の強さを表現する。

    Args:
        num1 (float): 変動前の値
        num2 (float): 変動後の値

    Returns:
        str: 変動の強さ
    """
    sharply_text: str
    substantially_text: str
    slightly_text: str
    difference = abs(num1 - num2)

    if difference > 50:
        return sharply_text
    if difference > 20:
        return substantially_text
    else:
        return slightly_text


def convert_to_past_tense(verb: str) -> str:
    """動詞を過去形に変換する。

    Args:
        verb (str): 動詞

    Returns:
        str: 変換後の動詞
    """
    end_char: str = verb[-1]

    if verb in INFINITIVE_VERB.keys():
        return INFINITIVE_VERB[verb]

    elif end_char == "e":
        verb += "d"
        return verb

    elif end_char == "y":
        end_char_2: str = verb[-2]
        if end_char_2 not in ["a", "e", "i", "o", "u"]:
            verb = verb[:-1] + "i"

    verb += "ed"
    return verb


def show_days_from_today(date: datetime.date) -> datetime.timedelta:
    """今日と対象日の日付の差を出力する。

    Args:
        date (datetime.date): 対象日

    Returns:
        datetime.timedelta: 今日と対象日の日付の差
    """
    return datetime.date.today() - date


def append_date_dif(sentence: str, date: datetime.date) -> str:
    """今日と対象日の日付の差を文章に追加します。

    Args:
        sentence (str): 文章
        date (datetime.date): 日付

    Returns:
        str: 変更後の文章
    """
    dif = show_days_from_today(date).days
    dif_year = dif / 365

    if dif > 0:
        sentence += str(math.floor(dif_year))
        sentence += " years ago."

    else:
        sentence += str(math.floor(dif_year))
        sentence += " years later."

    return sentence
