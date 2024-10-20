from functools import partial

t1_2_elems = {"Po_210": 138.356, "Po_198": 64.8,"Po_214": 0.1643,"Po_190": 19.7, "Po_216": 0.145}
# Словарь с периодами полураспада для разных изотопов полония
radioactive_funcs = {"Po_210": None, "Po_198": None, "Po_214": None, "Po_190": None, "Po_216": None,}
# Словарь для хранения каррированных функций

def f1(N0: float, t: int, t1_2=None) -> float:
    N = N0 * (1 / 2) ** (t / t1_2)
    res1 = "Масса радиоактивного вещества Po_210, t1_2=" + str(t1_2)

    print(f'{res1}1 с периодом полураспада {t1_2}, N0 = {N0}, t={t}')

    return N
def f2(N0: float, t: int, t1_2=None) -> float:
    N = N0 * (1 / 2) ** (t / t1_2)
    res1 = "Масса радиоактивного вещества Po_198, t1_2=" + str(t1_2)

    print(f'{res1}1 с периодом полураспада {t1_2}, N0 = {N0}, t={t}')

    return N
def f3(N0: float, t: int, t1_2=None) -> float:
    N = N0 * (1 / 2) ** (t / t1_2)
    res1 = "Масса радиоактивного вещества Po_214, t1_2=" + str(t1_2)

    print(f'{res1}1 с периодом полураспада {t1_2}, N0 = {N0}, t={t}')

    return N
def f4(N0: float, t: int, t1_2=None) -> float:
    N = N0 * (1 / 2) ** (t / t1_2)
    res1 = "Масса радиоактивного вещества Po_190, t1_2=" + str(t1_2)

    print(f'{res1}1 с периодом полураспада {t1_2}, N0 = {N0}, t={t}')

    return N
def f5(N0: float, t: int, t1_2=None) -> float:
    N = N0 * (1 / 2) ** (t / t1_2)
    res1 = "Масса радиоактивного вещества Po_216, t1_2=" + str(t1_2)

    print(f'{res1}1 с периодом полураспада {t1_2}, N0 = {N0}, t={t}')

    return N

f1 = partial(f1, t1_2=t1_2_elems['Po_210'])
f2 = partial(f2, t1_2=t1_2_elems['Po_198'])
f3 = partial(f3, t1_2=t1_2_elems['Po_214'])
f4 = partial(f4, t1_2=t1_2_elems['Po_190'])
f5 = partial(f5, t1_2=t1_2_elems['Po_216'])



def main():
    radioactive_funcs["Po_210"] = f1
    radioactive_funcs["Po_198"] = f2
    radioactive_funcs["Po_214"] = f3
    radioactive_funcs["Po_190"] = f4
    radioactive_funcs["Po_216"] = f5


    print("Результат:",radioactive_funcs["Po_210"](100, 8.7))
    print("Результат:", radioactive_funcs["Po_198"](100, 8.7))
    print("Результат:", radioactive_funcs["Po_214"](60, 8.7))
    print("Результат:", radioactive_funcs["Po_190"](100, 8.7))
    print("Результат:", radioactive_funcs["Po_216"](150, 8.7))


main()