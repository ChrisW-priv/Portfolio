print("""
Najpierw podaj czy program ma liczyć funkcję dla punktów czy wzoru funkcji
Dla punktów wpisz:  "Points"
Dla wzoru funkcji:
> głównej           "Main"
> kanonicznej       "Canonic"

Następnie wpisz te wartości
Dla wzoru funkcji:
> ax^2 +bx +c  dla głównej
> a(x-p)^2 +q dla kanonicznej
Dla punktów:
> (x1,0) lub os= Xo
 (x2,0)
 (x3,y)
Jeśli wpisujesz punkty proszę zwróć uwagę na to by pkt. pierwszy i drugi to były miejsca zerowe.
Ew. jeśli nie masz podanych 2 pkt. zerowych tylko oś symetrii, oś symetrii wpisz na pierwszej pozycji

Niezależnie od tego co wpisujesz, proszę zwróć uwagę by współczynniki były razem z wartościami (np. -3, a nie - 3)
""")

try:
    while True:
        what_f = input("Co wpisujesz? ")
        if what_f == "k":
            break

        class Combined:
            def __init__(self, a, b, c):
                self.a = a
                self.b = b
                self.c = c
                self.delta = self.b * self.b - 4 * self.a * self.c
                self.p = -self.b / (2 * self.a)
                self.q = -self.delta / (4 * self.a)
                self.w = f"({self.p}, {self.q})"
                self.os = f"x = {self.p}"
                self.x1 = (-self.b - self.delta ** 0.5) / (2 * self.a)
                self.x2 = (-self.b + self.delta ** 0.5) / (2 * self.a)

            def zw(self):
                if self.a > 0:
                    return f"<{self.q}, + {...})"
                elif self.a < 0:
                    return f"(-{...}, {self.q}>"

            def mono(self):
                if self.a > 0:
                    return f"Funkcja rosnąca dla x w przedziale <{self.p}, {...})\n" \
                        f"Funkcja malejąca dla x w przedziale ({...}, {self.p}>"
                elif self.a < 0:
                    return f"Funkcja rosnąca dla x w przedziale ({...}, {self.p}>\n" \
                        f"Funkcja malejąca dla x w przedziale <{self.p}, {...})"

            def m0(self):
                if self.delta > 0:
                    return "2"
                elif self.delta == 0:
                    return "1"
                elif self.delta < 0:
                    return "0"

            def x0(self):
                if self.delta > 0:
                    return f"x1 = {self.x1}\nx2 = {self.x2}"
                elif self.delta == 0:
                    return -self.b / (2 * self.a)
                elif self.delta < 0:
                    return "nie ma miejsc zerowych"

            def wplus(self):
                if self.delta > 0:
                    if self.a > 0:
                        return f"Funkcja przyjmuje wartości dodatnie dla x w przedziale\n" \
                            f"({...}, {self.x1}) oraz({self.x2}, {...})\n" \
                            f"Funkcja przyjmuje wartości ujemne dla x w przedziale\n" \
                            f"({self.x1}, {self.x2})"
                    if self.a < 0:
                        return f"Funkcja przyjmuje wartości dodatnie dla x w przedziale\n" \
                            f"({self.x1}, {self.x2})\n" \
                            f"Funkcja przyjmuje wartości ujemne dla x w przedziale\n" \
                            f"({...}, {self.x1}) oraz ({self.x2}, {...})"
                if self.delta == 0:
                    if self.a > 0:
                        return f"Funkcja przyjmuje wartości dodatnie dla x należącego do\n" \
                            f"Liczb rzeczywistych - [{self.x0()}]\n" \
                            f"Funkcja nie przyjmuje wartości ujemnych, x należy do zbioru pustego"
                    elif self.a < 0:
                        return f"Funkcja nie przyjmuje wartości dodatnich, x należy do zbioru pustego\n" \
                            f"Funkcja przyjmuje wartości ujemne dla x należącego do\n" \
                            f"Liczb rzeczywistych - [{self.x0()}]"
                if self.delta < 0:
                    if self.a > 0:
                        return f"Funkcja przyjmuje wartości dodatnie w całym przedziale funkcji\n" \
                            f"Funkcja nie przyjmuje wartości ujemnych, x należy do zbioru pustego"
                    elif self.a < 0:
                        return f"Funkcja nie przyjmuje wartości dodatnich, x należy do zbioru pustego\n" \
                            f"Funkcja przyjmuje wartości ujemne w całym przedziale funkcji"

            def main(self):
                return f"{self.a}x^2 +({self.b})x +({self.c})\na = {self.a}   b = {self.b}   c = {self.c}"

            def canonic(self):
                return f"{self.a}(x - ({self.p}))^2 + ({self.q})\na = {self.a}   p = {self.p}   q = {self.q}"

            def numeric(self):
                if self.delta < 0:
                    return "nie ma postaci iloczynowej"
                elif self.delta == 0:
                    return f"(x - ({self.x0})^2"
                elif self.delta > 0:
                    return f"{self.a}(x - ({self.x1}))(x - ({self.x2}))\n" \
                        f"a = {self.a}    x1 = {self.x1}    x2 = {self.x2}"

        intake = ""

        A = 0
        B = 0
        C = 0
        P1 = ""
        P2 = ""
        P3 = ""

        if what_f == "Points":
            P1 = input("Pkt 1 > ")
            P2 = input("Pkt 2 > ")
            P3 = input("Pkt 3 > ")
        elif what_f != "Points":
            intake = input(" > ")

        if what_f == "Main":
            pos_x2 = intake.find("x^2")
            pos_x = intake.find("x ")

            A = float(intake[:pos_x2])
            B = float(intake[intake.find("x^2") + 3: pos_x])
            C = float(intake[pos_x + 1:])
        elif what_f == "Canonic":
            pos_x = intake.find("x")
            pos_n1 = intake.find("(")
            pos_n2 = intake.find(")")
            pos2 = intake.find("^2")
            P = -float(intake[pos_x + 1: pos_n2])
            Q = float(intake[pos2 + 2:])

            A = float(intake[:pos_n1])
            B = -P*2*A
            C = (4*A*Q + (-P*2*A)**2)/(4*A)
        elif what_f == "Points":
            X1 = 0
            X2 = 0

            p1_pos_n1 = P1.find("(")
            p1_pos_n2 = P1.find(")")

            p2_pos_n1 = P2.find("(")
            p2_pos_n2 = P2.find(")")

            p3_pos_n1 = P3.find("(")
            p3_pos_n2 = P3.find(")")

            p1_pos_coma = P1.find(",")
            p2_pos_coma = P2.find(",")
            p3_pos_coma = P3.find(",")

            if not P1.__contains__("os"):
                X1 = float(P1[p1_pos_n1 + 1:p1_pos_coma])
                X2 = float(P2[p2_pos_n1 + 1:p2_pos_coma])
            elif P1.__contains__("os"):
                value_os = float(P1[P1.find("=") + 1:])
                X2 = float(P2[p2_pos_n1 + 1:p2_pos_coma])
                X1 = 2 * value_os - X2

            X3 = float(P3[p3_pos_n1 + 1:p3_pos_coma])
            Y3 = float(P3[p3_pos_coma + 1:p3_pos_n2])

            A = Y3 / (X3 ** 2 - X1 * X3 - X2 * X3 + X1 * X2)
            B = -A * (X1 + X2)
            C = A * X1 * X2

        func = Combined(A, B, C)

        print(f'''
Delta = {func.delta}

Postać główna = 
{func.main()}

Postać kanoniczna = 
{func.canonic()}

Postać iloczynowa = 
{func.numeric()}

{func.mono()}

{func.wplus()}

Wierzchołek (i wektor przesunięcia) = {func.w}

Zbiór wartości = {func.zw()}
Oś symetrii {func.os}

Liczba miejsc zerowych = {func.m0()}
Miejsce(miejsca) zerowe = 
{func.x0()}
''')
except ValueError and ZeroDivisionError and TypeError and NameError and SyntaxError:
    print("""
No i nie napisałeś/łaś tak jak prosiłem!
Teraz włącz program jeszcze raz i zrób wszystko jeszcze raz
TYM RAZEM DOKŁADNIE!!!
""")
