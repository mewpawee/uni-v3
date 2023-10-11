import math

# univ3 using Q64.96
q96 = 2**96


def price_to_tick(p):
    return math.floor(math.log(p, 1.0001))


def price_to_sqrtp(p):
    return int(math.sqrt(p) * q96)


print("Price 5000 to tick: ", price_to_tick(5000))
print("Price 5000 to sqrt(P) in Q96 form: ", price_to_sqrtp(5000))
