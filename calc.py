def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Błąd: Nie można dzielić przez zero"

print("Wybierz operację:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

wybor = input("Podaj numer operacji (1/2/3/4): ")

if wybor in ('1', '2', '3', '4'):
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        print(liczba1, "+", liczba2, "=", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print(liczba1, "-", liczba2, "=", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print(liczba1, "*", liczba2, "=", mnozenie(liczba1, liczba2))
    elif wybor == '4':
        print(liczba1, "/", liczba2, "=", dzielenie(liczba1, liczba2))
else:
    print("Błąd: Nieprawidłowy numer operacji.")
