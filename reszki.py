import random

heads = 0
tails = 0

times = int(input(" > "))
num = 0
while num < times:
    i = random.randint(0, 1)
    if i == 1:
        heads += 1
    elif i == 0:
        tails += 1
    num += 1

print("num of times heads occured: " + str(heads))
print("num of times tails occured: " + str(tails))
