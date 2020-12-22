empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = [even, odd]
print(numbers)

t = ("a", "b", "c")
print(t)

a = b = c = d = e = f = 12
print(c)

# Unpacking a tuple
x, y, z, (a, b, c) = 1, 2, 76, (1, 3, 4)
print(x)
print(y)
print(z)
print(a)

for t in enumerate("abcdefghi"):
    print(t)
