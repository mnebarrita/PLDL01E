# Initialization
basic_pay = 0
overtime_pay = 0
absence_deduction = 0
tardy_deduction = 0
honorarium = 0
gross_income = 0
total_deductions = 0
net_pay = 0
withholding_tax = 0
sss_contri = 0
philhealth_contri = 0
HDMF_contri = 100

# Input Employee Information
company_name = str(input("Enter Company Name: "))
department = str(input("Enter Department: "))
employee_code = float(input("Enter Employee Code: "))
employee_name = str(input("Enter Name of Employee: "))

# Input Pay Period
start_date = input("Enter the start date of the pay period (MM/DD/YYYY): ")
end_date = input("Enter the end date of the pay period (MM/DD/YYYY): ")
pay_period = f"{start_date} to {end_date}"

# Input Payroll Details
rate_per_hour = float(input("Enter Rate per hour: "))
hrs_worked = float(input("Enter Number of Hours Worked: "))
overtime_hrs = float(input("Enter Number of Overtime Hours: "))
absence_hrs = float(input("Enter Number of Absence Hours: "))
honorarium_amount = float(input("Enter Honorarium Amount: "))
tardy_hrs = float(input("Enter Number of Tardy Hours: "))

# Compute Gross Income
basic_pay = rate_per_hour * hrs_worked
overtime_pay = rate_per_hour * overtime_hrs
absence_deduction = rate_per_hour * absence_hrs
tardy_deduction = rate_per_hour * tardy_hrs
honorarium = honorarium_amount  # Set honorarium to input value

gross_income = basic_pay + overtime_pay + honorarium

# SSS Contribution based on Gross Income
if 0 <= gross_income < 4250:
    sss_contri = 180
elif 4250 <= gross_income <= 4749.99:
    sss_contri = 202.50
elif 4750 <= gross_income <= 5249.99:
    sss_contri = 225
elif 5250 <= gross_income <= 5749.99:
    sss_contri = 247.50
elif 5750 <= gross_income <= 6249.99:
    sss_contri = 270
elif 6250 <= gross_income <= 6749.99:
    sss_contri = 292.50
elif 6750 <= gross_income <= 7249.99:
    sss_contri = 315.00
elif 7250 <= gross_income <= 7749.99:
    sss_contri = 337.50
elif 7750 <= gross_income <= 8249.99:
    sss_contri = 360
elif 8250 <= gross_income <= 8749.99:
    sss_contri = 382.50
elif 8750 <= gross_income <= 9249.99:
    sss_contri = 405
elif 9250 <= gross_income <= 9749.99:
    sss_contri = 427.50
elif 9750 <= gross_income <= 10249.99:
    sss_contri = 450
elif 10250 <= gross_income <= 10749.99:
    sss_contri = 472.50
elif 10750 <= gross_income <= 11249.99:
    sss_contri = 495
elif 11250 <= gross_income <= 11749.99:
    sss_contri = 517.50
elif 11750 <= gross_income <= 12249.99:
    sss_contri = 540
elif 12250 <= gross_income <= 12749.99:
    sss_contri = 562.50
elif 12750 <= gross_income <= 13249.99:
    sss_contri = 585
elif 13250 <= gross_income <= 13749.99:
    sss_contri = 607.50
elif 13750 <= gross_income <= 14249.99:
    sss_contri = 630
elif 14250 <= gross_income <= 14749.99:
    sss_contri = 652.50
elif 14750 <= gross_income <= 15249.99:
    sss_contri = 675
elif 15250 <= gross_income <= 15749.99:
    sss_contri = 697.50
elif 15750 <= gross_income <= 16249.99:
    sss_contri = 720
elif 16250 <= gross_income <= 16749.99:
    sss_contri = 742.50
elif 16750 <= gross_income <= 17249.99:
    sss_contri = 765
elif 17250 <= gross_income <= 18249.99:
    sss_contri = 787.50
elif 17750 <= gross_income <= 18749.99:
    sss_contri = 810
elif 18250 <= gross_income <= 19749.99:
    sss_contri = 832.50
elif 18750 <= gross_income <= 19249.99:
    sss_contri = 855
elif 19250 <= gross_income <= 19749.99:
    sss_contri = 877.50
else:
    sss_contri = 900

# Withholding Tax Calculation
if 0 <= gross_income <= 20832.99:
    withholding_tax = 0.00
elif 20833 <= gross_income <= 33332:
    withholding_tax = 0.15 * (gross_income - 20833)
elif 33333 <= gross_income <= 66666:
    withholding_tax = 1875 + 0.20 * (gross_income - 33333)
elif 66667 <= gross_income <= 166666:
    withholding_tax = 8541.80 + 0.25 * (gross_income - 66667)
elif 166666 <= gross_income <= 666666:
    withholding_tax = 33541.80 + 0.30 * (gross_income - 166667)
else:
    withholding_tax = 183541.80 + 0.35 * (gross_income - 666667)

# PhilHealth Contribution Calculation
if gross_income == 10000:
    philhealth_contri = 500
elif 10000.01 <= gross_income <= 99999.99:
    philhealth_contri = gross_income * 0.05
elif gross_income == 100000:
    philhealth_contri = 5000

# Compute Total Deductions and Net Pay
total_deductions = (absence_deduction + tardy_deduction +
                    withholding_tax + sss_contri +
                    philhealth_contri + HDMF_contri)
net_pay = gross_income - total_deductions

# Print Statements
print("Company Name: ", company_name)
print("Employee Code: ", employee_code)
print("Employee Name: ", employee_name)
print("Department: ", department)
print("Pay Period: ", pay_period)
print("Basic Pay: ", basic_pay)
print("Overtime Pay: ", overtime_pay)
print("Absence Deduction: ", absence_deduction)
print("Tardy Deduction: ", tardy_deduction)
print("Honorarium: ", honorarium)
print("Withholding Tax: ", withholding_tax)
print("SSS Contributions: ", sss_contri)
print("PhilHealth Contributions: ", philhealth_contri)
print("HDMF Contributions: ", HDMF_contri)
print("Total Deductions: ", total_deductions)
print("Gross Earnings: ", gross_income)
print("Net Pay: ", net_pay)

#tapos naaa