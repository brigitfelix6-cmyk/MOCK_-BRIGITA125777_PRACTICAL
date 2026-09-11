employee_id=(input("enter employee id"))
employee_name=(input ("enter employee name"))
basic_salary=int(input("enter the basic salary"))
allowance=int(input("enter the allowance"))
deduction=int(input ("enter deduction"))
tax_rate=0.1
gross_salary=basic_salary+allowance
tax_amount=gross_salary*tax_rate
net_salary=gross_salary-deduction-tax_amount
print("employee_id:", employee_id)
print("employee name:",employee_name)
print("basic salary:",basic_salary)
print("allowance:",allowance)
print("deduction:",deduction)
print("tax_amount:",tax_amount)
print("gross_salary:",gross_salary)
print("net_salary:",net_salary)