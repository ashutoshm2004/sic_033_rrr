# Tax Calculator Problem
# GlobalNext Solutions, a rapidly growing IT company, employs a diverse workforce ranging from entry-
# level developers to senior executives. The HR department wants to streamline the tax calculation
# process for employees under the New Tax Regime (2023). They’ve decided to build a tax calculation
# program that computes salaries, taxes, and net incomes while ensuring compliance with the latest tax
# laws.
# As a software developer in GlobalNext’s HR-Tech team, you are tasked with developing this program.
# The system should process employee salary details, validate inputs, calculate taxes, and generate
# detailed reports.
# Objectives
# The program should:
# 1. Accept employee details, including monthly salary components.
# 2. Calculate gross and taxable income according to the New Tax Regime (2023).
# 3. Compute the tax payable using the appropriate tax slabs.
# 4. Apply any applicable standard deductions and rebates.
# 5. Generate reports detailing gross salary, taxable income, tax payable, and net salary.
# Level 1: Basic Input and Salary Calculation
# Objective: Capture employee details and calculate the gross salary.
# Tasks:
# • Accept the following inputs for an employee:
# o Name
# o EmpID
# o Basic Monthly Salary
# o Special Allowances (Monthly)
# o Bonus Percentage (Annual Bonus as % of Gross Salary)
# • Calculate:
# o Gross Monthly Salary = Basic Salary + Special Allowances
# o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus
# • Output:
# o Display the employee details, gross monthly salary, and annual gross salary.


name                    = input("Enter the name of the employee: ")
emp_id                  = input("Enter the employee ID: ") 
basic_monthly_salary    = float(input("Enter the Basic Monthly Salary: "))
special_allowance       = float(input("Enter the Special Monthly Allowance: "))
bonus_percentage        = float(input("Enter the annual bonus: "))

gross_monthly_salary = basic_monthly_salary + special_allowance
annual_gross_salary = (gross_monthly_salary*12) + (bonus_percentage*gross_monthly_salary)

print("Employee Name: ", name)
print("Employee ID: ", emp_id)
print("Gross Monthly Salary: ", gross_monthly_salary)
print("Annual Gross Salary: ",annual_gross_salary)
