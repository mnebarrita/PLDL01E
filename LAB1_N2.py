#Initialization of the name, net income, gross income, total deduction, and pag-ibig contribution
emp_name =""
net_inc =0
gross_inc =0
total_deduction =0
pagibig_contri =100

#Input the employees name and the value of rate per hour, number of hours per day, number of days per week, number of weeks per month, SSS contribution, Philhealth contribution, and Tax contribution
emp_name =str(input("Enter employee's name: "))
rate_per_hr =float(input("Enter rate per hour: "))
num_hrs_per_day =float(input("Enter number of hours per day: "))
num_days_per_week =float(input("Enter number of days per week: "))
num_weeks_per_month =int(input("Enter number of weeks per month: "))
SSS_contri =float(input("Enter the value of SSS contribution: "))
philhealth_contri =float(input("Enter the value of PhilHealth contribution: "))
tax_contri =float(input("Enter the value of Tax contribution: "))

#Computing the value of the Gross Income, Total Deduction, and the Net Income
gross_inc =rate_per_hr * num_hrs_per_day * num_days_per_week * num_weeks_per_month
total_deduction =SSS_contri + philhealth_contri + pagibig_contri
net_inc =gross_inc - total_deduction

#Display Employee's Name, Net Income, Gross Income, and Total Deduction
print ("Employee's Name: ", emp_name)
print ("Net Income: ", net_inc)
print ("Gross Income: ", gross_inc)
print ("Total Deduction: ", total_deduction)