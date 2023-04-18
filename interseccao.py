import re

def linear_eq_to_points(eq):
    # Extração de coeficientes
    coefs = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', eq)
    a, b, c = [float(i) for i in coefs]

    x_int = c / a if a != 0 else None
    y_int = c / b if b != 0 else None

    # Calcula os dois pontos
    if x_int is not None and y_int is not None:
        p1 = (x_int, 0)
        p2 = (0, y_int)
    elif x_int is not None:
        p1 = (x_int, 0)
        p2 = (x_int + 1, 0)
    else:
        p1 = (0, y_int)
        p2 = (0, y_int + 1)

    l = (p1[0], p2[1])
    return l

def intersection(l1, l2):
    m1, b1 = l1
    m2, b2 = l2
    
    if m1 == m2:
        return None
    else:
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        return (x, y)

eq1 = "2x + 3y = 6"
eq2 = "-1x + 2y = 2"
l1 = linear_eq_to_points(eq1)
l2 = linear_eq_to_points(eq2)
resultado = intersection(l1, l2)
if resultado is None:
    print("As linhas não se encontram")
else:
    print("As linhas se encontram no ponto:", resultado)