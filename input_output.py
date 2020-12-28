# jabber = open("/Users/jackjutzi/sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line)
#
# jabber.close()

with open("/Users/jackjutzi/sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

cities = []

with open("/Users/jackjutzi/cities.txt") as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)

with open("/Users/jackjutzi/sample.txt", 'a') as jabber:
    for i in range(1, 13):
        result = i*2
        print("{0} times 2 is {1}".format(i, result), file=jabber)
    print("-"*20, file=jabber)

for m in dir(__builtins__):
    print(m)