names1 = ["Xena", "Bozsi", "Vica", "Szonja", "Eni", "Ildi", "Zsuzsi", 11, True]
names2 = ["Pista", "Balázs", "Kornél", "Levente", "Gyuszi"]


def nev_printer(nev_lista):
    for nev in nev_lista:
        if isinstance(nev, str):
            print(nev.upper())
        else:
            print(nev, "-->", "Is not a string", str(type(nev)))


nev_printer(names1)
nev_printer(names2)
