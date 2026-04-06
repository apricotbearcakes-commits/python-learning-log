count = 1

while count <= 5:
    print(count)
    count = count + 1
  
number = int(input("数字を入力してください："))
count = 1

while count <= number:
    if count % 2 == 0:
        print(count)
    count = count + 1

print(4 % 2)
print(5 % 2)
print(6 % 2)
print(7 % 2)

number = int(input("数字を入力してください："))
count = 1
total = 0

while count <= number:
    total = total + count
    count = count + 1

print(f"合計：{total}")
