import random


def sum_up(a, b):
    return a + b


sum_up_lambda = lambda a, b: a + b


def get_random_int():
    random_int = random.randint(100, 200)
    return random_int


list_1 = ["a", "p", "p", "l", "e"]
list_2 = ["m", "a", "n", "g", "o"]


def string_list_to_string(string_list):
    word = ""
    for char in string_list:
        word += char
    return word


print(sum_up(3, 4))
print(sum_up_lambda(1, 2))
print(get_random_int())
print(get_random_int())
print(string_list_to_string(list_1))
print(string_list_to_string(list_2))
