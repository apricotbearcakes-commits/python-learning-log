person = {"name": "Masako", "job": "Data Annotator", "city": "Sunnyvale"}

print(person["name"])
print(person["job"])
print(person["city"])

person = {"name": "Masako", "job": "Data Annotator"}

person["city"] = "Sunnyvale"
print(person)

person["job"] = "Python Developer"
print(person)

person = {"name": "Masako", "job": "Data Annotator", "city": "Sunnyvale"}

for key in person:
    print(key, ":", person[key])

person = {"name": "Masako", "job": "Data Annotator", "city": "Sunnyvale", "hobby": "Design", "goal": "Apple"}

for key in person:
    print(key, ":", person[key])


