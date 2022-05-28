student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}






# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_scores[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_scores[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_scores[key] = "Acceptable"
    else:
        student_scores[key] = "Fail"
    student_grades[key] = student_scores[key]
print(student_grades)





