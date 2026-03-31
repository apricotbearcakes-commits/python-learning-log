name = input("名前を入力してください：")
age = int(input("年齢を入力してください："))

if age >= 18:
    print(f"{name}さん、ようこそ！")
else:
    print(f"{name}さん、まだ入場できません")
