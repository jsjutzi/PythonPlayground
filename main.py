computer_parts = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse mat"
]

print(computer_parts)

data = [4, 5, 104, 105, 110, 120, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)
data.reverse()
print(data)

