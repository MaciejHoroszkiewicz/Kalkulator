import logging 
logging.basicConfig(level=logging.DEBUG)

#def calculator(x, y):
calculate = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2: Odejmowanie, 3: Mnożenie, 4: Dzielenie\n")
if calculate == "1":
    x = input("Podaj składnik 1: ")
    y = input("Podaj składnik 2: ")
    logging.info(f"Dodaję {x} do {y}")
    if "." in x or "." in y:
        print(f"Wynik to {float(x) + float(y)}")
    else:
        print(f"Wynik to {int(x) + int(y)}")
elif calculate == "2":
    x = input("Podaj składnik 1: ")
    y = input("Podaj składnik 2: ")
    logging.info(f"Odejmuję {x} od {y}.")
    if "." in x or "." in y:
        print(f"Wynik to {float(x) - float(y)}")
    else:
        print(f"Wynik to {int(x) - (int(y))}")
elif calculate == "3":
    x = input("Podaj składnik 1: ")
    y = input("Podaj składnik 2: ")
    logging.info(f"Mnożę {x} i {y}")
    if "." in x or "." in y:
        print(f"Wynik to {float(x) * float(y)}")
    else:
        print(f"Wynik to {int(x) * int(y)}")
elif calculate == "4":
    x = input("Podaj składnik 1: ")
    y = input("Podaj składnik 2: ")
    logging.info(f"Dzielę {x} przez {y}")
    if y == "0":
        print("Nie można dzielić przez zero!")
    else:
        if "." in x or "." in y:
            print(f"Wynik to {float(x) // float(y)}")
        else:
            print(f"Wynik to {int(x) // int(y)}")