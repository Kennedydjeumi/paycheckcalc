def multiply_hourly(rate, hours):
    Money = rate * hours
    tax = Money * 0.15
    Net = Money - tax
    return Net
def salary(salary):
  Money=salary
  taxes= Money * 0.15
  net= Money - taxes
  return net

print("Paycheck calculator:\nHow often do you get paid?")
options = ["weekly", "semimonthly"]
other_pay="Salary"
print("Or do you get paid in {} ".format(other_pay))

while True:
    for option in options:
        print(option)

    choice = input("").lower()

    if choice == "weekly":
        try:
            Weeklypay = float(input("What is your hourly rate? "))
            hours_worked = float(input("How many hours have you worked? "))
            print("Your check will be", multiply_hourly(Weeklypay, hours_worked))
            break  
        except ValueError:
            print("Numerical values only, please try again.")
    elif choice == 'semimonthly':
        try:
            Semimonthlypay = float(input("What's your hourly rate? "))
            hours_worked = float(input("How many hours have you worked? "))
            print("Your check will be", multiply_hourly(Semimonthlypay, hours_worked))
            break  
        except ValueError:
            print("Numerical values only, please try again.")
    
    if choice == "salary": 
        try:
            Salary_input=float(input("What is your salary "))
            print("By your salary you should have made ",salary(Salary_input))
            break 
        except ValueError:
            print("Numerical values only, please try again.")

     
   