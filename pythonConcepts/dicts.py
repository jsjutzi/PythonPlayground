fruits = {"apple": "sweet, crunchy fruit", "banana": "soft, yellow fruit", "lemon": "yellow, firm, bitter fruit",
          "pear": "odd shaped apple", "grape": "small, round seed fruit", "orange": "large round citrus fruit"}

# print(fruits)
#
# while True:
#     dict_key = input("Enter a fruit to search: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruits:
#         description = fruits.get(dict_key)
#         print(description)
#     else:
#         print("No such fruit recognized")

print(fruits.keys())
print(fruits.values())
print(fruits.items())
