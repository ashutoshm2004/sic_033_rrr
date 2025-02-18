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
#------------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------
# Level 2: Taxable Income Calculation
# Objective: Calculate taxable income after standard deductions.
# Tasks:
# • Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
# • Compute the Taxable Income and display all intermediate calculations.
# Output: Display gross salary, standard deduction and taxable income.
#----------------------------------------------------------------------------------------------
# Level 3: Tax and Rebate Calculation
# Objective: Compute tax payable using the New Tax Regime (2023) slabs.
# Tasks:
# 1. Calculate tax based on the following slabs:
# o ₹0 - ₹3,00,000: 0%
# o ₹3,00,001 - ₹6,00,000: 5%
# o ₹6,00,001 - ₹9,00,000: 10%
# o ₹9,00,001 - ₹12,00,000: 15%
# o ₹12,00,001 - ₹15,00,000: 20%
# o Above ₹15,00,000: 30%
# 2. Apply Section 87A Rebate:
# o Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0).
# 3. Add a 4% Health and Education Cess to the calculated tax.
# Output:
# • Display a detailed tax breakdown, including slabs, cess, and total tax payable.

# -----------------------------------------------
# Level 4: Net Salary Calculation
# Objective: Calculate annual net salary after tax deductions.
# Tasks:
# 1. Compute Net Salary = Annual Gross Salary - Total Tax Payable.
# 2. Display:
# o Annual Gross Salary
# o Total Tax Payable (including cess)
# o Annual Net Salary
# --------------------------------------------
# Level 6: Input Validation Rules
# Objective: Validate all inputs to ensure accuracy and correctness.
# Validation Rules:
# 1. Employee Details:
# o Name: Non-empty, alphabets only, max 50 characters.
# o EmpID: Alphanumeric, 5–10 characters.
# 2. Salary Inputs:
# o Basic Salary: Positive number, max ₹1,00,00,000.
# o Special Allowances: Non-negative, max ₹1,00,00,000.
# o Bonus Percentage: Numeric value, 0–100.
# 3. Derived Calculations:
# o Gross Monthly Salary must be greater than zero.
# o Annual Gross Salary should not exceed realistic values.
# 4. General:
# o Reject invalid inputs with a clear error message.
# o Provide re-entry prompts for invalid data.
# Output:
# • Indicate if any inputs are invalid and prompt for correction.
# --------------------------------------------------
# Level 5: Report Generation
# Objective: Generate a detailed report for employees.
# Tasks:
# 1. Summarize all computed details:
# o Employee Details (Name, EmpID)
# o Gross Monthly Salary
# o Annual Gross Salary
# o Taxable Income
# o Tax Payable (with breakdown)
# o Annual Net Salary
# 2. Format the output as a report for better readability.
# Output:
# • Provide a clean, tabular report for employees.
# Example Output (For Reports Level)
# Employee Tax Report
# Field Details
# Name John Doe
# EmpID E12345
# Gross Monthly Salary ₹85,000
# Annual Gross Salary ₹10,20,000
# Taxable Income ₹9,70,000
# Tax Payable ₹76,800
# Annual Net Salary ₹9,43,200


name                    = input("Enter the name of the employee: ")
emp_id                  = input("Enter the employee ID: ") 
basic_monthly_salary    = float(input("Enter the Basic Monthly Salary: "))
special_allowance       = float(input("Enter the Special Monthly Allowance: "))
bonus_percentage        = float(input("Enter the annual bonus: "))

gross_monthly_salary    = basic_monthly_salary + special_allowance
annual_gross_salary     = (gross_monthly_salary*12) + (bonus_percentage*(gross_monthly_salary*12)/100)
taxable_income          = annual_gross_salary - 50000

print("Employee Name            : ", name)
print("Employee ID              : ", emp_id)
print("Gross Monthly Salary     : ", gross_monthly_salary)
print("Annual Gross Salary      : ",annual_gross_salary)
print("Taxable Income           : ",taxable_income)

print("-"*50)

print(f'%-20s : {name}' %("Employee Name"))
print(f'%-20s : {emp_id}' %("Employee ID"))
print(f'%-20s : {gross_monthly_salary}' %("Gross Monthly Salary"))
print(f'%-20s : {annual_gross_salary}' %("Annual Gross Salary"))
print(f'%-20s : {taxable_income}' %("Taxable Income"))

if (taxable_income>0 and taxable_income<=300000):
    tax_p=0
elif (taxable_income>300000 and taxable_income<=600000):
    tax_p=5
elif (taxable_income>600000 and taxable_income<=900000):
    tax_p=10
elif (taxable_income>900000 and taxable_income<=1200000):
    tax_p=15
elif (taxable_income>1200000 and taxable_income<=1500000):
    tax_p=20
elif (taxable_income>1500000):
    tax_p=30

if (taxable_income<=700000):
    rebate_p=100
    tax_payable=0
else:
    reabate_p=0
    tax_payable=taxable_income*tax_p /100

cess=tax_payable+(0.04*taxable_income)

print(tax_payable+cess)
