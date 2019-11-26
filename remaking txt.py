new_file = "/Users/Chris/Documents/copy.txt"
with open(new_file, "r") as txt:
    refactored = ""
    for lin in txt:
        for ch in lin:
            if ch == "\t":
                ch = "*znak tabulacji*"
                refactored += ch
            elif ch == "\n":
                ch = "*nowa linia*"
                refactored += ch
            else:
                refactored += ch

    line = refactored.split("*nowa linia*")

    jednoliscienne = ""
    dwuliscienne = ""

    for item in line:
        kategorie = (item.split("*znak tabulacji*"))
        cecha = kategorie.__getitem__(0)
        jedno = kategorie.__getitem__(1)
        dwu = kategorie.__getitem__(2)
        jednoliscienne += jedno + "\n"
        dwuliscienne += dwu + "\n"

    print(jednoliscienne)
    print(dwuliscienne)

with open("new_txt.txt", "w") as new:
    new.write(jednoliscienne + "\n" + dwuliscienne)
