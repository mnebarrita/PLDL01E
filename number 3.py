#Initialization
rate_per_hour = 0
number_of_working_hours_per_day = 0
number_of_days_per_week = 0
number_of_weeks_per_month = 0
employee_name = ""
department = ""
total_deduction = 0
gross_income = 0
net_income = 0
SSS_contri = 0
phil_contri = 0
love_contri = 100

#input

employee_name = str(input("Enter Employee Name: "))
department = str(input("Enter Department: "))
rate_per_hour = float(input("Enter Rate Per Hour: "))
number_of_working_hours_per_day = float(input("Enter Number of Working Hours per Day: "))
number_of_days_per_week = float(input("Enter Number of Days per Week: "))
number_of_weeks_per_month = float(input("Enter Number of Weeks per Month: "))

#Calculate
gross_income =(number_of_working_hours_per_day * number_of_days_per_week * number_of_weeks_per_month * rate_per_hour)

# Function to determine sss contributions
def calculate_SSS_contri (gross_income):
     if gross_income <= 20000:
        return 100
     elif gross_income <= 50000:
        return 1200
     elif gross_income <= 75000:
         return 6800
     else:
        return 8800

# Function to determine philhealth contribution
def calculate_phil_contri(gross_income):
    if gross_income <= 20000:
        return 125.75
    elif gross_income <= 50000:
        return 2200.50
    elif gross_income <= 75000:
        return 4800
    else:
        return 5800

#Calculate SSS and Philhealth contributions
SSS_contri = calculate_SSS_contri(gross_income)
phil_contri = calculate_phil_contri(gross_income)

#Calculate Total Deduction
total_deduction = (SSS_contri + love_contri + phil_contri)

#Calculate Net Income
net_income = (gross_income - total_deduction)

#print  results
print("\n --- EMPLOYEE INCOME SUMMARY")
print(f"Employee Name: {employee_name}")
print(f"Department: {department}")
print (f"Gross Income: {gross_income: .2f}")
print(f"Total Deduction: {total_deduction: .2f}")
print(f"Net Income: {net_income: .2f}")



