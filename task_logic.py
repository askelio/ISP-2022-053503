from statistics import median
import re
import operator


def get_text(path):
    f = open(path, 'r')
    text = f.read()
    print(text)
    return text


def aw_words_count(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    denominator = len(sentences)
    numerator = 0

    for i in sentences:
        words = re.sub(r'\W', ' ', i).split()
        numerator += len(words)
    return int(numerator / denominator)


def rep_words(text):
    words = re.sub(r'\W', ' ', text).split()
    w_table = dict()

    counter = 0
    for i in words:
        for j in words:
            if i == j:
                counter += 1
        w_table[i] = counter
        counter = 0

    sort = sorted(w_table.items(), key=operator.itemgetter(1), reverse=True)
    sorted_table = dict(sort)
    return sorted_table


def median_words_number(text):
    return median([len(sentence.split()) for sentence in text.split(".")])


def top_k_m(k, m, text):
    words = re.sub(r'\W', ' ', text).split(' ')
    new_text = ''.join(words)

    table = dict()

    for i in range(len(new_text) - m + 1):
        counter = 0
        for j in range(len(new_text) - m + 1):
            if new_text[i:i + m] == new_text[j:j + m]:
                counter += 1
        table[new_text[i:i + m]] = counter

    sort = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
    sorted_table = dict(sort)

    i = 0
    for key, value in sorted_table.items():
        if i >= k:
            break
        print("{0}: {1}".format(key, value))
        i += 1
