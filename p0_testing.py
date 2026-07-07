scores = [85, 92, 78, 90, 66, 100, 73]
print(scores[2])
print(scores[-2:])

passing = [score for score in scores if score >= 80]
print(passing)
print(len(passing))

student = {"name": "Amy", "score": 92, "grade": "A"}

score = student.get("score", 0)

print(score)
if score >= 80:
    student["passed"] = True
else:
    student["passed"] = False
print(student)

students = [
    {"name": "Amy", "score": 92},
    {"name": "Ben", "score": 65},
    {"name": "Cara", "score": 88},
]
names = [student["name"] for student in students if student["score"] >= 80]
print(names)


temps = [15, 22, 18, 30, 12, 27, 19, 33, 8, 25]
print(temps[0 : len(temps) : 2])

new_list = ["hot" if temp > 25 else temp for temp in temps]
print(new_list)
print(len([temp for temp in temps if temp < 20]))
