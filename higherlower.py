import random
from replit import clear

import art
from game_data import data

NUMBER_OF_DATA = 50


# Generate a random number
def generate_number():
    rand_num = random.randint(0, NUMBER_OF_DATA - 1)
    return rand_num


def printer(position_in, number_in):
    name = data[number_in]["name"]
    position = position_in
    description = data[number_in]["description"]
    country = data[number_in]["country"]
    if position == 'A':
        print(f"Compare {position}: {name}, {description}, from {country}.")
    else:
        print(f"Against {position}: {name}, {description}, from {country}.")


num1 = generate_number()
num2 = generate_number()
score = 0
game_going = True
while game_going:
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    printer('A', num1)
    print(art.vs)
    printer('B', num2)
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_input == "a":
        if data[num1]["follower_count"] > data[num2]["follower_count"]:
            score += 1
            num1 = num2
            num2 = generate_number()
        else:
            clear()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score is: {score}")
            game_going = False
    elif user_input == "b":
        if data[num1]["follower_count"] < data[num2]["follower_count"]:
            score += 1
            num1 = num2
            num2 = generate_number()
        else:
            game_going = False
            clear()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score is: {score}")

# print(data[num1]['name'])
