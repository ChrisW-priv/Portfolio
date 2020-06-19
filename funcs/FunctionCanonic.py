print("""
Wpisz kanoniczną postać funkcji kwadratowej
   a(x -p)^2 +q
Znaki współczynników MUSZĄ być razem żeby program działał poprawnie
""")


class FunctionCanonic:
    def __init__(self, a, p, q):
        self.a = a
        self.b = -p*2*a
        self.c = (4*a*q + self.b*self.b)/(4*a)
        self.delta = self.b*self.b - 4*self.a*self.c
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

pos_x = intake.find("x")
pos_n1 = intake.find("(")
pos_n2 = intake.find(")")
pos2 = intake.find("^2")

A = float(intake[:pos_n1])
P = float(intake[pos_x+1: pos_n2])
Q = float(intake[pos2+2:])

func = FunctionCanonic(A, -P, Q)

print(f'''
wierzchołek (i wektor przesunięcia) = {func.w}
{func.mono()}
zbiór wartości = {func.zw()}
oś symetrii = {func.os}
Liczba miejsc zerowych = {func.m0()}
miejsce(miejsca) zerowe = {func.x0()}
delta = {func.delta}  
postać główna = {func.main()}

postać kanoniczna = {func.canonic()}

postać iloczynowa = {func.numeric()}
''')
