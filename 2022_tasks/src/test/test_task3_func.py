from main.task3_func import (
    append_date_dif,
    append_min_max,
    append_verb,
    convert_to_past_tense,
    create_sentence,
    should_connect_two_sentences,
    show_change_strength,
    show_days_from_today,
    summerize_sentence,
)


def test_connect_two_sentences():
    assert should_connect_two_sentences(1, 1) == True
    assert should_connect_two_sentences(1, 2) == False
    assert should_connect_two_sentences(-2, 2) == False


def test_append_min_max():
    assert append_min_max(15.5, "The number ") == "The number peaked"
    assert append_min_max(3.11, "The price ") == "The price hit a low"
    assert append_min_max(7.54, "The best record of malathon ") == "The best record of malathon "
