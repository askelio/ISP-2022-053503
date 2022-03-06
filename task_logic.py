import operator


def get_top_k(k, m, text):
    new_text = ""

    for i in text:
        if i.isalpha():
            new_text += i

    print(new_text)

    table = dict()

    for i in range(len(new_text) - m + 1):
        counter = 0
        for j in range(len(new_text) - m + 1):
            if new_text[i:i + m] == new_text[j:j + m]:
                counter += 1
        table[new_text[i:i + m]] = counter

    sort = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
    sorted_table = dict(sort)

    i = k
    for word, key in sorted_table.items():
        if i <= 0:
            break
        print(word, key)
        i -= 1
