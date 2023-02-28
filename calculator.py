import logging 
logging.basicConfig(level=logging.DEBUG)


#def calculator(x, y):
def calculate(operation):
    x = input("Podaj składnik 1: ")
    y = input("Podaj składnik 2: ")

    if operation == "1":
        logging.info(f"Dodaję {x} do {y}")
        if "." in x or "." in y:
            result = float(x) + float(y)
        else:
            result = int(x) + int(y)
    elif operation == "2":
        logging.info(f"Odejmuję {x} od {y}.")
        if "." in x or "." in y:
            result = float(x) - float(y)
        else:
            result = int(x) - int(y)
    elif operation == "3":
        logging.info(f"Mnożę {x} i {y}")
        if "." in x or "." in y:
            result = float(x) * float(y)
        else:
            result = int(x) * int(y)
    elif operation == "4":
        logging.info(f"Dzielę {x} przez {y}")
        if y == "0":
            logging.warning("Nie można dzielić przez zero!")
            result = None
        else:
            if "." in x or "." in y:
                result = float(x) // float(y)
            else:
                result = int(x) // int(y)

    return result

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2: Odejmowanie, 3: Mnożenie, 4: Dzielenie\n")
result = calculate(operation)
print(f"Wynik to {result}.")
