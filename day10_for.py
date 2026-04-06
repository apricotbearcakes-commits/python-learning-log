for count in range(1, 6):
    print(count)

for count in range(3, 8):
    print(count)

for count in range(0, 10, 2):
    print(count)

total = 0
for count in range(1, 11):
    total = total + count

print(f"合計：{total}")

number = int(input("数字を入力してください："))
total = 0
for count in range(1, number + 1):
    total = total + count

print(f"合計：{total}")

name = input("名前を入力してください：")

for i in range(5):
    print(name)

name = input("名前を入力してください：")

for i in range(1, 6):
    print(f"{i}回目：{name}")
