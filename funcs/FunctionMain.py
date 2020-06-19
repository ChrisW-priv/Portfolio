print("""
Wpisz główną postać funkcji kwadratowej
   ax^2 +bx +c
Znaki współczynników MUSZĄ być razem żeby program działał poprawnie
""")


class FunctionMain:
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
            return f"""
funkcja rosnąca dla x w przedziale <{self.p}, {...})
funkcja malająca dla x w przedziale ({...}, {self.p}>"""
        elif self.a < 0:
            return f"""
funkcja rosnąca dla x w przedziale ({...}, {self.p}>
funkcja malająca dla x w przedziale <{self.p}, {...})"""

    def m0(self):
        if self.delta > 0:
            return "2"
        elif self.delta == 0:
            return "1"
        elif self.delta < 0:
            return "0"

    def x0(self):
        if self.delta > 0:
            return f"""
x1 = {self.x1}
x2 = {self.x2}"""
        elif self.delta == 0:
            return -self.b / (2 * self.a)
        elif self.delta < 0:
            return "nie ma miejsc zerowych"

    def main(self):
        return f"""
{self.a}x^2 +({self.b})x +({self.c})
a = {self.a}   b = {self.b}   c = {self.c}"""

    def canonic(self):
        return f"""
{self.a}(x - ({self.p}))^2 + ({self.q})
a = {self.a}   p = {self.p}   q = {self.q}"""

    def numeric(self):
        if self.delta < 0:
            return "nie ma postaci iloczynowej"
        elif self.delta == 0:
            return f"(x - ({self.x0})^2"
        elif self.delta > 0:
            return f"""
{self.a}(x - ({self.x1}))(x - ({self.x2}))
a = {self.a}    x1 = {self.x1}    x2 = {self.x2}"""


intake = input(" > ")

pos_x2 = intake.find("x^2")
pos_x = intake.find("x ")

A = float(intake[:pos_x2])
B = float(intake[intake.find("x^2") + 3: pos_x])
C = float(intake[pos_x + 1:])

func = FunctionMain(A, B, C)

print(f'''
wierzchołek (i wektor przesunięcia) = {func.w}
{func.mono()}
zbiór wartości = {func.zw()}
oś symetrii {func.os}
Liczba miejsc zerowych = {func.m0()}
miejsce(miejsca) zerowe = {func.x0()}
delta = {func.delta}  
postać główna = {func.main()}

postać kanoniczna = {func.canonic()}

postać iloczynowa = {func.numeric()}
''')
