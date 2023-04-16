words_list = ['attribute', 'класс', 'функция', 'type']


def is_written_byte(sequence):
    for item in sequence:
        try:
            print(eval(f'b"{item}"'))
        except SyntaxError:
            print(f'word: «{item}» is not possible to write in bytes format')


is_written_byte(words_list)