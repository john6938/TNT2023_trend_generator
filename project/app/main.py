import random

MAX_SENTENCE_NUM = 4
MIN_BANANA_NUM = 0
MAX_BANANA_NUM = 10


def generate_banana_num():
    return random.randint(MIN_BANANA_NUM, MAX_BANANA_NUM)


subjects = ["The number of bananas", "The number", "It"]
increase_words = ["increases", "rises", "grows"]
unchanged_words = ["remains the same", "remains flat", "stays flat"]
decrease_words = ["decreases", "falls", "declines"]
prepositions = ["from", "to", "by"]

sentences = []
num_bananas = [generate_banana_num()]

for i in range(MAX_SENTENCE_NUM):
    num_bananas.append(generate_banana_num())
    subject = subjects[i % len(subjects)]

    if num_bananas[i + 1] > num_bananas[i]:
        verb = increase_words[i % len(increase_words)]
    elif num_bananas[i + 1] == num_bananas[i]:
        verb = unchanged_words[i % len(unchanged_words)]
    else:
        verb = decrease_words[i % len(unchanged_words)]

    # TODO Add prepositions to complete the sentence.
    #
    # For example (If there is any difference of numbers):
    #   rand_num1 = random.randint(0, len(prepositions))
    #   rand_num2 = rand_num1.copy()
    #   while(rand_num1 == rand_num2)
    #       rand_num2 = random.randint(0, len(prepositions))
    #   preposition1 = prepositions[rand_num1]
    #   preposition2 = prepositions[rand_num2]
    #   ...

    sentences.append(" ".join([subject, verb]))
    sentences[i] += "."
    print(sentences[i])
