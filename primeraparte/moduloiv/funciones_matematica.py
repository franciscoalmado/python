def f(x):
    return 5 * x + 3

y = f(10)

print(y)

def raices(a, b, c):
    d = (b**2 - 4*a*c) ** 0.5
    x1 = (-b + d) / 2*a
    x2 = -(-b + d) / 2*a
    return [x1, x2]

print(raices(1, 1, -6))