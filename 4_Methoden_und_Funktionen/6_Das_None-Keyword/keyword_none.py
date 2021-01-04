a = 5 # Wie wenn später setzen?
a = None

print(a)

def add(a, b):
    if a is None:
        a = 5
    a = a + 5
    return a

c = add(a, 6)
print(c)