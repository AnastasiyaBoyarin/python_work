byte_format = [b'class', b'function', b'method']


def get_type_content_length_variables(sequence):
    for item in sequence:
        print(f'type: {type(item)} | content: {item} | length: {len(item)}')


get_type_content_length_variables(byte_format)