print("Введите сумму чисел: ")
x = int(input())

print("Введите произведение чисел: ")
y = int(input())

for i in range(x):
    for j in range(y):
        if (x == i + j) and (y == i * j):
            print(f'{i}, {j}')
