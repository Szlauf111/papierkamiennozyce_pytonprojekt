import random

zwyGracza = 0
zwyBota = 0

print("witam w grze papier, kamien, nozyce")

print("1. papier")
print("2. kamien")
print("3. nozyce \n")

y = int(input("Podaj ile rund chcesz zagrac: "))

for x in range (y):

    los = random.randrange(1, 4)
    liczba = int(input("Podaj co wybierasz: "))

    if liczba == 1:
        print("\n wybrales papier \n")
    elif liczba == 2:
        print("\n wybrales kamien \n")
    elif liczba == 3:
        print("\n wybrales nozyce \n")
    else:
        print("zly wybor")
        exit

    if los == 1:
        print(" komputer wybral papier\n")
    elif los == 2:
        print(" komputer wybral kamien\n")
    elif los == 3:
        print(" komputer wybral nozyce\n")

    if liczba == los:
        print("remis \n ===================================================== ")
        zwyGracza = zwyGracza + 0
        zwyBota = zwyBota + 0
    elif liczba == 1:
        if los == 2:
            print("wygrales \n ===================================================== ")
            zwyGracza = zwyGracza + 1
        elif los == 3:
            print("przegrales \n ===================================================== ")
            zwyBota = zwyBota + 1

    elif liczba == 2:
        if los == 3:
            print("wygrales \n ===================================================== ")
            zwyGracza = zwyGracza + 1
        elif los == 1:
            print("przegrales \n ===================================================== ")
            zwyBota = zwyBota + 1

    elif liczba == 3:
        if los == 1:
            print("wygrales \n ===================================================== ")
            zwyGracza = zwyGracza + 1
        elif los == 2:
            print("przegrales \n ===================================================== ")
            zwyBota = zwyBota + 1

print("koniec meczu. Ostateczy wynik")
print("Twoje punkty: ")
print(zwyGracza)
print("punkty komputera: ")
print(zwyBota)

if zwyGracza > zwyBota:
    print("gratulacje wygrales gre!")
elif zwyBota > zwyGracza:
    print("Niestety nie udalo ci sie wygrac :(")
else:
    print("remis")
    print("dogrywka do 1 punkta")
    while zwyGracza == 1 or zwyBota == 1:
        los = random.randrange(1, 4)
    liczba = int(input("Podaj co wybierasz: "))

    if liczba == 1:
        print("\n wybrales papier \n")
    elif liczba == 2:
        print("\n wybrales kamien \n")
    elif liczba == 3:
        print("\n wybrales nozyce \n")
    else:
        print("zly wybor")
        exit

    if los == 1:
        print(" komputer wybral papier\n")
    elif los == 2:
        print(" komputer wybral kamien\n")
    elif los == 3:
        print(" komputer wybral nozyce\n")

    if liczba == los:
        print("remis \n ===================================================== ")
        zwyGracza = zwyGracza + 0
        zwyBota = zwyBota + 0
    elif liczba == 1:
        if los == 2:
            print("wygrales \n ===================================================== ")
            zwyGracza = zwyGracza + 1
        elif los == 3:
            print("przegrales \n ===================================================== ")
            zwyBota = zwyBota + 1

    elif liczba == 2:
        if los == 3:
            print("wygrales \n ===================================================== ")
            zwyGracza = zwyGracza + 1
        elif los == 1:
            print("przegrales \n ===================================================== ")
            zwyBota = zwyBota + 1

    elif liczba == 3:
        if los == 1:
            print("wygrales \n ===================================================== ")
            zwyGracza = zwyGracza + 1
        elif los == 2:
            print("przegrales \n ===================================================== ")
            zwyBota = zwyBota + 1
    if zwyGracza > zwyBota:
        print("gratulacje wygrales dogrywke!")
    elif zwyBota > zwyGracza:
        print("Niestety nie udalo ci sie wygrac dogrywki:(")