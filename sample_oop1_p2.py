class Employee_Info:

    def __init__(self):
        self.company_name = ""
        self.emp_department = ""
        self.emp_name = ""
        self.emp_code = ""
        self.salary_cut_off = ""

    # 1 usage
    def get_emp_data(self, company_name, emp_department, emp_name, emp_code, salary_cut_off):
        self.company_name = company_name
        self.emp_department = emp_department
        self.emp_name = emp_name
        self.emp_code = emp_code
        self.salary_cut_off = salary_cut_off

    # 1 usage
    def display_data(self):
        print("Company Name: ", self.company_name)
        print("Employee Department:", self.emp_department)
        print("Employee Name:", self.emp_name)
        print("Employee Code:", self.emp_code)
        print("Cut-Off Date:", self.salary_cut_off)

    def get_basic_pay(self, emp_rate_per_hour, emp_num_of_hours_per_payday):
        self.basic_pay = emp_rate_per_hour * emp_num_of_hours_per_payday
        return self.basic_pay

    # 1 usage

    def get_absences_deduction(self, emp_rate_per_hour, emp_num_of_absences):
        self.emp_absences = emp_num_of_absences * emp_rate_per_hour
        return self.emp_absences

    def get_overtime_pay(self, emp_hour_overtime, emp_rate_per_hour):
        self.overtime_pay = self.emp_hour_overtime * emp_rate_per_hour
        return self.overtime_pay

    def get_tardiness_deduction(self, emp_rate_per_hour, tardiness_num_hours):
        self.tardiness_deduction = tardiness_num_hours * emp_rate_per_hour
        return self.tardiness_deduction
import sample_oop1_p1

obj = sample_oop1_p1.Employee_Info()

company = input("Enter company name: ")
department = input("Enter employee department: ")
employee_name = input("Enter employee name: ")
employee_code = input("Enter employee number or code: ")
salary_cutoff = input("Enter salary cut off: ")

obj.get_emp_data(company, department, employee_name, employee_code, salary_cutoff)

# data entry for basic pay computation
obj = sample_oop1_p1.Employee_Salary()

rate_pay = float(input("Enter employee rate per hour: "))
number_working_hours = float(input("Enter employee number of working hours: "))
honorarium_pay = float(input("Enter honorarium pay: "))
number_absences = float(input("Enter number of absences in hours: "))

# computation for basic pay
basic_pay = obj2.get_basic_pay(rate_pay, number_working_hours)
absences_deduction = obj2.get_absences_deduction(rate_pay, number_absences)

# display of output
print("____________________________________________________________________")
print("____________________________________________________________________")
obj2.desiplay_data()
print("Basic Pay: $.2f" % basic_pay)
print("Honararium Pay: %.2f" % honorarium_pay)
print("Employee absences deduction: %.2f" % absences_deduction)
print("____________________________________________________________________")
print("____________________________________________________________________")