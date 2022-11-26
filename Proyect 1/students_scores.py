student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville":62,
}
student_grades = {}
for keys in student_scores:
    if student_scores[keys] > 90 and student_scores[keys] <=100:
        student_grades[keys] = "Outstanding"
    if student_scores[keys] > 80 and student_scores[keys] <=90:
        student_grades[keys] = "Exceeds Expectations"
    if student_scores[keys] > 70 and student_scores[keys] <=80:
        student_grades[keys] = "Acceptable"
    if student_scores[keys] <= 70:
        student_grades[keys] = "Fail"
print(student_grades.items())