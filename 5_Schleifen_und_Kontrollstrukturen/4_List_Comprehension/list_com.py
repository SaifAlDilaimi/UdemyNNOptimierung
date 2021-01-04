squares = []

for x in range(10):
    squares.append(x**2)

#print(squares)

squares_comp = [x**2 for x in range(10)]
#print(squares_comp)

txt = "Hallo 1234 Welt"
numbers = [int(n) for n in txt if n.isdigit()]
#print(numbers)

numbers = []
for n in range(10):
    if n % 2 == 0:
        numbers.append(1)
    else:
        numbers.append(0)
#print(numbers)

# mit list comp?
#numbers = [1 for n in range(10) if n%2 == 0]
numbers = [1 if n%2 == 0 else 0 for n in range(10)]
#print(numbers)

# mehrere schleifen
# [1,2,3,4], [5, 6, 7, 8, 9] -> [5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 15, 18, 21, 24, 27, 20, 24, 28, 32, 36]
numbers = []
for i in range(1, 5):
    for j in range(5, 10):
        numbers.append(i * j)
print(numbers)

numbers = [i * j for i in range(1, 5) for j in range(5, 10)]
print(numbers)

