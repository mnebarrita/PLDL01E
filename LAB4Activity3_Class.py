import datetime

class Student:
    def __init__(self):
        self.student_name = input("Enter Student Name: ")
        self.student_number = input("Enter Student Number: ")
        self.course = input("Enter Course: ")
        self.year_level = input("Enter Year Level: ")
        self.sections = input("Enter sections: ").split(',')
        self.subjects = input("Enter subjects (comma-separated): ").split(',')
        self.enrolled_units = int(input("Enter number of units enrolled: "))
        self.unit_cost = 1551.00
        self.miscellaneous_fees = float(input("Enter Miscellaneous fees: "))
        self.downpayment = float(input("Enter Downpayment amount: "))
        self.payment_terms = input("Enter payment terms (e.g., Prelims, Midterms, Finals): ").split(',')
        self.date_printed = datetime.datetime.now().strftime("%Y-%m-%d")

    def compute_total_fees(self):
        self.tuition_fee_lecture = self.enrolled_units * self.unit_cost
        self.assessment_amt = self.tuition_fee_lecture + self.miscellaneous_fees
        self.total_due = self.assessment_amt + self.downpayment

    def split_payments(self):
        self.payment_schedule = {term: self.total_due / len(self.payment_terms) for term in self.payment_terms}

    def display_info(self):
        print(f"Student Name: {self.student_name}")
        print(f"Student Number: {self.student_number}")
        print(f"Course: {self.course}")
        print(f"Year Level: {self.year_level}")
        print(f"Sections: {self.sections}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Tuition Fee (Lecture): {self.tuition_fee_lecture:.2f}")
        print(f"Miscellaneous Fees: {self.miscellaneous_fees:.2f}")
        print(f"Assessment Amount: {self.assessment_amt:.2f}")
        print(f"Downpayment: {self.downpayment:.2f}")
        print(f"Total Due: {self.total_due:.2f}")
        print(f"Date Printed: {self.date_printed}")
        for term, amount in self.payment_schedule.items():
            print(f"{term}: {amount:.2f}")

class FeeAssessment:
    def __init__(self):
        self.students = []

    def add_student(self):
        student = Student()
        student.compute_total_fees()
        student.split_payments()
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()
            print('-' * 30)