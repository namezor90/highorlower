import random
from art import logo, vs
from game_data import data

print(logo)

def follower_check(data1, data2):
    check = ""
    if data1["follower_count"] > data2["follower_count"]:
        check = "a"
    elif data1["follower_count"] < data2["follower_count"]:
        check = "b"
    return check

def random_vs_random():
    game_data = random.sample(data, 2)
    data1 = game_data[0]
    data2 = game_data[1]
    return data1, data2

def save_good(data1, data2):
    temp = ""
    check = follower_check(data1, data2)
    if check == "a":
        temp = data1
    elif check == "b":
        temp = data2
    return temp

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    account_follower = account["follower_count"]
    return f"{account_name}, a {account_descr}, from {account_country}: Psszzzz! {account_follower}"

game = True
point = 0
temp = {}
while game:
    data1, data2 = random_vs_random()

    if temp != {}:
        data1 = temp


    print(f"Compare A: {format_data(data1)}.")
    print(vs)
    print(f"Compare A: {format_data(data2)}.")
    choice = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
    if choice == follower_check(data1, data2):
        point += 1
        print(f"You're right! Current score: {point}")
        temp = save_good(data1, data2)
    elif choice != follower_check(data1, data2):
        print(f"Sorry, that's wrong. Final score: {point}")
        game = False
