#1 msol
# students = {
#     "Ali":[80,90,85],
#     "Vali":[70,60,75],
#     "Sami":[95,88,92]
# }
# for ism,rating in students.items():
#     print(f"{ism}ning o'rtacha bahosi: ",end=" ")
#     print(min(rating))

#2 msol
# products = [
#     {"name":"olma", "price":120},
#     {"name":"anor", "price":90},
#     {"name":"banan", "price":150}
# ]
# for product in products:
#     if product["price"] > 100:
#         print(f"{product}")

#3 misol
# users = [
#     {"name":"Ali", "age":20},
#     {"name":"Vali", "age":16},
#     {"name":"Sami", "age":25}
# ]
# for user in users:
#     if user["age"] > 18:
#         print(f"{user}")

#4 msol
# courses = {
#     "python":["Ali", "Vali", "Sami"],
#     "django":["Ali","Sami"],
#     "ai":["Vali","Sami","Jasur"]
# }
# for course in courses:
#     print(f"{course} guruhida: {len(courses[course])}")

#4 msol
# data = {
#     "users":[
#         {"name":"Ali","activ    e":True},
#         {"name":"Vali", "active":False},
#         {"name":"Sami", "active":True}
#     ]
# }
# for user in data["users"]:
#     if user["active"]:
#         print(f"{user}")

# 5 msol
numbers = [
    [4,7,2],
    [9,1,5],
    [3,8,6]
]
max_number = numbers[0][0]

for qator in numbers:
    for number in qator:
        if number > max_number:
            max_number = number
        print(max_number)