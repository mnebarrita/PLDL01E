from LAB4Activity3_Class import Student, FeeAssessment

# LAGYAN M VALUE SA ASSESSMENT FEES and
class FirstImage(Student):
    def display_info():
        #Assessment of Fees #
        print(f"Tuition Fee Lecture: ")
        print(f"AdU CHRONICLE")
        print(f"ATHLETIC")
        print(f"AUDIO-VISUAL LIBRARY")
        print(f"AUSG")
        print(f"CULTURAL FEE")
        print(f"ENERGY COST, AIRCON CLASSROOM")
        print(f"GUIDANCE")
        print(f"INSURANCE FEE")
        print(f"LEARNING MANAGEMENT SYSTEM")
        print(f"LIBRARY FEE")
        print(f"MEDICAL AND DENTAL")
        print(f"REGISTRATION")
        print(f"RSO")
        print(f"STUDENT ACTIVITIES FEE")
        print(f"STUDENT NURTURANCE FEE")
        print(f"TECHNOLOGY FEE")
        print(f"TEST PAPERS")
        print(f"")

assessment = FeeAssessment()
assessment.add_student()
more_students = input("Do you want to add more students? (yes/no): ").lower()
while more_students == 'yes':
    assessment.add_student()
    more_students = input("Do you want to add more students? (yes/no): ").lower()

assessment.display_all_students()
