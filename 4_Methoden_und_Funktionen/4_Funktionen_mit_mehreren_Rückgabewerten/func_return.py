def f(x):
    y0 = x * 2
    y1 = x
    y2 = x / 2

    return y0, y1, y2

result = f(5)
print(result, type(result))

y0, y1, y2 = f(5)
print(y0)
print(y1)
print(y2)