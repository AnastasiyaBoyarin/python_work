import random
from random import randint

amount_coin = int(input('введите количество монет: '))
m = 0
k = 0
coins = [0, 1]
for i in range(amount_coin):
    random.shuffle(coins)
    print(f'все монеты {coins}')
    if int(coins[0]) == 0:
        m += 1
    else:
        k += 1
print(f'всего монет {m, k}')

if m > k:
    ans = k
else:
    ans = m

print(f"минимальное количество монет, которые нужно перевернуть {ans}")