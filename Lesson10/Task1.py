letter_format = ['разработка', 'сокет', 'декоратор']
hardcoded_format = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']


def check_type_content(sequence):
    for item in sequence:
        print(f'type: {type(item)} | content: {item}')


def check_type_content_by_using_encode(sequence):
    for item in sequence:
        print(item.encode('unicode_escape'))
        print(f'type: {type(item)} | content: {item}')


check_type_content(letter_format)
check_type_content(hardcoded_format)
check_type_content_by_using_encode(letter_format)
