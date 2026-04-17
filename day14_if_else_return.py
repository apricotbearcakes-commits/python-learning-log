def add(a, b):
    return a + b

result = add(10, 5)
print(result)


def check_score(name, score):
    if score >= 80:
        return (f"{name}さん！合格です！")
    else:
        return (f"{name}さん！不合格です！")

print(check_score("Masako", 85))
print(check_score("Hana", 60))
