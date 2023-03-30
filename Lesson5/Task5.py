def ascii_recursion(ascii_code):
    if ascii_code == 128:
        return
    else:
        print("%4d-%s" % (ascii_code, chr(ascii_code)), end='')
        if ascii_code % 10 == 0:
            print()
    ascii_recursion(ascii_code + 1)


ascii_recursion(32)
