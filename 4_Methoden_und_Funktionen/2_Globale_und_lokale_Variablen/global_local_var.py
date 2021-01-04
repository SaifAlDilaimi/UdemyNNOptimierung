# global variable
def f():
    print(s)

s = "Hallo Saif"
f()

# local variable
def f2():
    s = "Hallo Tom"
    print(s)

f2()
print(s)

# global und local
def f3():
    s = "Hallo Tom"
    print(s)

s = "Hallo Saif"
f3()
print(s)

# global und local kombinieren!
def f4():
    global s # Extra fehler, erstmal ohne global
    print(s) # Extra fehler, erstmal ohne global
    s = "Hallo Tom"
    print(s)

s = "Hallo Saif"
f4()
print(s)

