names1 = ["Xena", "Bozsi", "Vica", "Szonja", "Eni", "Ildi", "Zsuzsi", 11, True]
names2 = ["Pista", "Balázs", "Kornél", "Levente", "Gyuszi"]


def nev_printer(name_list):
    for name in name_list:
        if isinstance(name, str):
            print(name.upper())
        else:
            print(name, "-->", "Is not a string", str(type(name)))


nev_printer(names1)
nev_printer(names2)
