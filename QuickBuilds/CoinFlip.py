from random import random

times = int(input(" > How many tosses? "))

heads = 0
for _ in range(times):
    heads += 1*(random()>0.5)

print("number of times heads occured: " + str(heads))
print(f"number of times tails occured: {times-heads}")

deviation = (abs(times/2-heads) / times * 100)*2
print(f'deviation: {round(deviation, 3)}%')
