hour = int(input("時間を入力してください："))

if hour >= 6 and hour < 12:
    print("おはようございます")
elif hour >= 12 and hour < 18:
    print("こんにちは")
elif hour >= 18 and hour < 23:
    print("こんばんは")
else:
    print("おやすみなさい")
