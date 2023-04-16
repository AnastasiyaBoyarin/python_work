words_list = ['разработка', 'администрирование', 'protocol', 'standard']


def convert_words_and_reverse(sequence):
    for item in sequence:
        bytes_word = str.encode(item, encoding='utf-8')
        string_word = bytes.decode(bytes_word, encoding='utf-8')
        print(f'Word «{item}» in bytes state «{bytes_word}» and '
              f'vice versa «{string_word}»')


convert_words_and_reverse(words_list)