student_scores = {
    "harry" : 81,
    "ron" : 78,
    "tom" : 98,
    "don" : 74,
    "navin" : 62,
}

student_grade = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grade[student] = "super"
    elif score > 80:
        student_grade[student] = "exelent"
    elif score > 70:
        student_grade[student] = "good"
    else:
        student_grade[student] = "avg"

print(student_grade)