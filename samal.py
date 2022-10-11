import math 
from tabulate import tabulate
from sympy import *
def bissiton():
    def foncution(x):
        return math.exp(x) - 2*(x)**2
    a = int(input('donne le a = '))
    b = int(input('donne le b = '))
    epselon = float(input("donne la epselon : "))

    # a=1
    # b=2
    c = (b + a)/2
    delta = b - a
    table = [["a","b", "c", "fa", "fb", "fc", "delta"],[round(a, 3), round(b, 3), round(c, 3), round(foncution(a), 3), round(foncution(b), 3), round(foncution(c), 3), round(delta, 3)]]

    while delta >= epselon:
        c = (b +a)/2
        if foncution(a) * foncution(b) < 0:
            b = c
        else:
            a = c
        delta = b - a
        table.append([round(a, 3), round(b, 3), round(c, 3), round(foncution(a), 3), round(
            foncution(b), 3), round(foncution(c), 3), round(delta, 3)
        ])

    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


def newton_raphson():
    def f1(x):
        return x**3 - 2*x**2 + x - 2

    def df(x):
        return 3*x**2 - 4*x + 1
    # epselon = input("donne la epselon : ")
    # table = ["n","x0","xn","dx"]

    def exsection() : 
        # table1 = []
        # table2 = []
        n = 0
        x0 = float(input("donne la x0 : "))
        epselon = float(input("donne la epselon : "))
        xn = x0 - f1(x0) / df(x0)
        dx = x0 - xn
        # print(n, "|", round(x0, 3), "|", round(xn, 3), "|", round(dx, 3))
        tap = [["n","x0","xn","dx"],[n, round(x0, 3), round(xn, 3), round(dx, 3)]]
        while (dx >= epselon):
            x0 = xn
            xn = x0 - f1(x0) / df(x0)
            dx = x0 - xn
            n+=1
            # print(n, "|", round(x0, 3), "|", round(xn, 3), "|", round(dx, 3))
            tap.append([n, round(x0, 3), round(xn, 3), round(dx, 3)])
    # exsection()
        print(tabulate(tap, headers='firstrow', tablefmt='fancy_grid'))
    exsection()


exs = input("you want  methode bissiton wright yes ")



if (exs == "yes") :
    bissiton()
else :
    newton_raphson()
