import random

isFinished = False
sum_of_random_ints = 0

while not isFinished:
    random_int = random.randint(10, 30)
    print(random_int)
    if random_int == 15 or random_int == 25:
        isFinished = True
        break
    sum_of_random_ints += random_int

print(sum_of_random_ints)
