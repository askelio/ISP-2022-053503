import task_logic as tl


def main():
    try:
        text = tl.get_text('text')

        print('The number of repeated words in the text: ')
        for key, value in tl.rep_words(text).items():
            print("{0}: {1}".format(key, value))

        print()
        print('Average number of words in a sentence: ',
              tl.aw_words_count(text), '\n')

        print('Median number of words in a sentence: ',
              tl.median_words_number(text), '\n')

        print('Enter M,K values (1) K=10 | M = 4   (2) Your onw values')
        m = 4
        k = 10
        tmp = int(input('Enter the number: '))
        if tmp == 2:
            k = int(input('Enter K value: '))
            m = int(input('Enter M value: '))

        print()
        print('Top K most frequently repeated letter N-grams: ')
        tl.top_k_m(k, m, text)
    except Exception as e:
        print(e)
        print('Restart the program to enter correct values')


if __name__ == "__main__":
    main()
