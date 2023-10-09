import random

rand_int_1 = random.randint(0, 100)
rand_int_2 = random.randint(0, 100)
print("1:", rand_int_1, "2:", rand_int_2)

if rand_int_1 < rand_int_2 and rand_int_1 < 50:
    print("Number 1 is smaller than number 2 as well as Mini")
if rand_int_1 < 30 or rand_int_2 < 30:
    print("One of the two numbers is smaller than 30")
if rand_int_1 < 50 and rand_int_2 != 50:
    print("Number 1 is small and number 2 is not a fifty")
