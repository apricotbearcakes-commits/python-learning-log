fruits = ["apple", "banana", "mango"]
print(fruits)

fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

fruits = ["strawberry", "pear", "fig"]

for fruit in fruits:
    print(fruit)

fruits = ["strawberry", "pear", "fig"]

print(len(fruits))
fruits.append("mango")
print(fruits)
fruits.remove("pear")
print(fruits)

fruits = ["strawberry", "pear", "fig"]

print("--- 元のリスト ---")
for fruit in fruits:
    print(fruit)

fruits.append("mango")

print("--- 追加後 ---")
for fruit in fruits:
    print(fruit)

colors = ["red", "blue", "green"]

print("--- 元のリスト ---")
for color in colors:
    print(color)

colors.remove("blue")

print("--- 削除後 ---")
for color in colors:
    print(color)
