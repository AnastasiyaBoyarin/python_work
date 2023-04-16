import subprocess
import chardet

tasks = (['ping', 'yandex.ru'], ['ping', 'youtube.com'])


def decode_subprocess(task):
    process = subprocess.Popen(task, stdout=subprocess.PIPE)
    own_encoding = 'utf-8'
    for line in process.stdout:
        response = chardet.detect(line)
        specific_encoding = response['encoding']
        print(f'Process transfers data in the following encoding'
              f' {specific_encoding}')
        in_its_encoding = line.decode(specific_encoding).encode(own_encoding)
        result = in_its_encoding.decode(own_encoding)
        print(result)


for item in tasks:
    print(item[1].upper())
    decode_subprocess(item)