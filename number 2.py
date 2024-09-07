#Initialization
final_grade = 0
final_quizzes = 0
final_assignment = 0
final_exam = 0
final_project = 0


#Input
student_name = str(input("Enter Student Name: "))
final_quizzes = float(input("Enter Final Quiz Grade: "))
final_assignment = float(input("Enter Final Assignment Grade: "))
final_exam = float(input("Enter your Final Exam Grade: "))
final_project = float(input("Enter your Final Project Grade: "))


#Calculate final grade
final_grade = (0.30 * final_quizzes) + (0.10 * final_assignment) + (0.40 * final_exam) + (0.20 * final_project)


# Function to determine equivalent grade remark
def get_equivalent_grade(grade):
    if 98 <= grade <= 100:
        return 4.00
    elif 95 <= grade <= 97:
        return 3.75
    elif 92 <= grade <= 94:
        return 3.50
    elif 89 <= grade <= 91:
        return 3.25
    elif 86 <= grade <= 88:
        return 3.00
    elif 83 <= grade <= 85:
        return 2.75
    elif 80 <= grade <= 82:
        return 2.50
    elif 77 <= grade <= 79:
        return 2.25
    elif 74 <= grade <= 76:
        return 2.00
    elif 71 <= grade <= 73:
        return 1.75
    elif 68 <= grade <= 70:
        return 1.50
    elif 64 <= grade <= 67:
        return 1.25
    elif 60 <= grade <= 63:
        return 1.00
    else:
        equivalent_grade = "invalid"

# Equivalent Grade Remark
equivalent_grade = get_equivalent_grade(final_grade)

#Round the Final Grade
rounded_final_grade = round(final_grade, 2)

#Print the results
print("\n --- FINAL GRADE SUMMARY ---")
print("Student's Name: ", student_name)
print("Final Quiz Grade: ", final_quizzes)
print("Final Assignment Grade: ", final_assignment)
print("Final Project Grade: ", final_project)
print("Final Grade: ", rounded_final_grade)
print("Equivalent Grading Remark", equivalent_grade)