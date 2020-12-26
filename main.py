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


# Fibonacci:
def fibonacci(n: int) -> int:
    """Return the `n` th fibonacci number for positive `n` """
    if n <= 0 <= 1:
        return
    n_minus1, n_minus2 = 1, 0
    result = None

    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

#
# for i in range(36):
#     print(i, fibonacci(i))

numbers = (1, 2, 3, 4, 5)

# * character unpacks tuple
print(*numbers, sep="|")

# Fizzbuzz


def fizz_buzz(n: int) -> None:
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz!")
        elif i % 3 == 0:
            print("Fizz!")
        elif i % 5 == 0:
            print("Buzz!")
        else:
            print(i)


fizz_buzz(100)