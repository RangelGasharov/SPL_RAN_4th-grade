import random

random_int = random.randint(0, 100)
print(random_int)

if random_int < 20:
    print("Mini")
elif 20 <= random_int <= 50:
    print("Medium")
else:
    print("Large")
