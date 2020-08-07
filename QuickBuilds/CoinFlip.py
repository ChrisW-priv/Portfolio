import random

heads = 0; tails = 0

times = int(input(" > How many tosses? "))
for i in range(times):
    n = random.randint(0, 1)
    if n == 1:
        heads += 1
    else:
        tails += 1

print("num of times heads occured: " + str(heads))
print("num of times tails occured: " + str(tails))
