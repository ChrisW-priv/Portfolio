class QuadraticFunc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.delta = b**2 - 4*a*c
        self.p = -b / (2*a)
        self.q = -self.delta / (4 * a)
        self.os = f"x = {self.p}"
        self.x1 = (-b - self.delta ** 0.5) / (2 * a)
        self.x2 = (-b + self.delta ** 0.5) / (2 * a)

    def __repr__(self):
        return f"""
A = {self.a}\nB = {self.b}\nC = {self.c}\n\nDelta = {self.delta}\nW(p,q) = ({round(self.p, 3)}, {round(self.q, 3)})\noś symetrii: {self.os}\n\n\
x1 = {self.x1}\nx2 = {self.x2}\n\nZbiór wartości:\n{self.zw()}\n\nMonotoniczność:\n{self.mono()}\n\nMiejsca zerowe:\n{self.x0()}\n\n{self.wplus()}\n\n\
Postać kanoniczna:\n{self.canonic()}\n\nPostać iloczynowa:\n{self.numeric()}\n"""

    def zw(self):
        if self.a > 0:
            return f"<{self.q}, + {...})"
        elif self.a < 0:
            return f"(-{...}, {self.q}>"

    def mono(self):
        if self.a > 0:
            return  f"Funkcja malejąca dla x w przedziale ({...}, {self.p}>\n"\
                    f"Funkcja rosnąca dla x w przedziale <{self.p}, {...})"
                
        elif self.a < 0:
            return  f"Funkcja rosnąca dla x w przedziale ({...}, {self.p}>\n" \
                    f"Funkcja malejąca dla x w przedziale <{self.p}, {...})"

    def n_m0(self):
        if self.delta > 0:
            return 2
        elif self.delta == 0:
            return 1
        elif self.delta < 0:
            return 0

    def x0(self):
        if self.n_m0() == 0:
            return "nie ma miejsc zerowych"
        elif self.n_m0() == 1:
            return -self.b / (2 * self.a)
        elif self.n_m0() == 2:
            return f"x1 = {self.x1}\nx2 = {self.x2}"

    def wplus(self):
        if self.n_m0() == 2:
            if self.a > 0:
                return f"Funkcja przyjmuje wartości dodatnie dla x w przedziale\n" \
                    f"({...}, {self.x1}) oraz({self.x2}, {...})\n" \
                    f"Funkcja przyjmuje wartości ujemne dla x w przedziale\n" \
                    f"({self.x1}, {self.x2})"
            elif self.a < 0:
                return f"Funkcja przyjmuje wartości dodatnie dla x w przedziale\n" \
                    f"({self.x1}, {self.x2})\n" \
                    f"Funkcja przyjmuje wartości ujemne dla x w przedziale\n" \
                    f"({...}, {self.x1}) oraz ({self.x2}, {...})"
        elif self.n_m0() == 1:
            if self.a > 0:
                return f"Funkcja przyjmuje wartości dodatnie dla x należącego do\n" \
                    f"Liczb rzeczywistych - [{self.x0()}]\n" \
                    f"Funkcja nie przyjmuje wartości ujemnych, x należy do zbioru pustego"
            elif self.a < 0:
                return f"Funkcja nie przyjmuje wartości dodatnich, x należy do zbioru pustego\n" \
                    f"Funkcja przyjmuje wartości ujemne dla x należącego do\n" \
                    f"Liczb rzeczywistych - [{self.x0()}]"
        elif self.n_m0() == 0:
            if self.a > 0:
                return f"Funkcja przyjmuje wartości dodatnie w całym przedziale funkcji\n" \
                    f"Funkcja nie przyjmuje wartości ujemnych, x należy do zbioru pustego"
            elif self.a < 0:
                return f"Funkcja nie przyjmuje wartości dodatnich, x należy do zbioru pustego\n" \
                    f"Funkcja przyjmuje wartości ujemne w całym przedziale funkcji"

    def main(self):
        return f"{round(self.a, 3)}x^2 +({round(self.b, 3)})x +({round(self.c, 3)})\na = {self.a}\tb = {self.b}\tc = {self.c}"

    def canonic(self):
        return f"{round(self.a, 3)}(x - ({round(self.p, 3)}))^2 + ({round(self.q, 3)})\na = {self.a}\tp = {self.p}\tq = {self.q}"

    def numeric(self):
        if self.n_m0() == 0:
            return "nie ma postaci iloczynowej"
        elif self.n_m0() == 1:
            return f"(x - ({round(self.x, 3)})^2"
        elif self.n_m0() == 2:
            return f"{self.a}(x - ({round(self.x, 3)}))(x - ({round(self.x, 3)}))\n" \
                f"a = {self.a}\tx1 = {self.x1}\tx2 = {self.x2}"
