import random
from art import logo, vs
from game_data import data

print(logo)

def follower_check(data1, data2):
    """
    Összehasonlítja a data1 és data2 paraméterekben megadott "follower_count" értékeket, és visszatér
    a magasabb követőszámmal rendelkező adat azonosítójával.

    Paraméterek:
        data1 (dict): Az első összehasonlítandó adat.
        data2 (dict): A második összehasonlítandó adat.

    Visszatérési érték:
        str: "a" ha az első adat követőszáma nagyobb, "b" ha a másodiké nagyobb
    """
    check = ""
    if data1["follower_count"] > data2["follower_count"]:
        check = "a"
    elif data1["follower_count"] < data2["follower_count"]:
        check = "b"
    return check

def random_vs_random():
    """
    Véletlenszerűen kiválaszt két adatot a játék adatai közül összehasonlításra.

    Visszatérési érték:
        tuple: A kiválasztott data1 és data2 adatokat tartalmazó tuple.
    """
    game_data = random.sample(data, 2)
    data1 = game_data[0]
    data2 = game_data[1]
    return data1, data2

def save_good(data1, data2):
    """
    Ellenőrzi, melyik választás volt helyes ("a" vagy "b"), és eltárolja a nyertes adatot
    a következő fordulóhoz.

    Paraméterek:
        data1 (dict): Az első összehasonlítandó adat.
        data2 (dict): A második összehasonlítandó adat.

    Visszatérési érték:
        dict: A magasabb követőszámmal rendelkező fiók adatai
    """
    temp = ""
    check = follower_check(data1, data2)
    if check == "a":
        temp = data1
    elif check == "b":
        temp = data2
    return temp

def format_data(account):
    """
    Egy előre formázott szöveget készít az adott fiók adatai alapján.

    Paraméterek:
        account (dict): Az aktuális fiók adatai, amely tartalmazza a nevét, leírását, országát
                       és követőszámát.

    Visszatérési érték:
        str: A fiók adatait tartalmazó formázott szöveg
    """
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
    print(f"Compare B: {format_data(data2)}.")
    choice = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
    if choice == follower_check(data1, data2):
        point += 1
        print(f"You're right! Current score: {point}")
        temp = save_good(data1, data2)
    elif choice != follower_check(data1, data2):
        print(f"Sorry, that's wrong. Final score: {point}")
        game = False
