# coding: utf-8

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


values = [200, 100, 50, 20, 10, 5, 2, 1]

combos = 0

def get_decompositions(total, maximal_coin):
    global combos
    if total < 0:
        pass
    elif total == 0:
        combos += 1
    else:
        for value in values:
            if value <= maximal_coin:
                get_decompositions(total - value, maximal_coin = value)

get_decompositions(200, 200)
print combos
