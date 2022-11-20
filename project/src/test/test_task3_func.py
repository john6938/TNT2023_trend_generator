from app.task3_func import (
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
