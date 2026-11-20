print("Hello Github!")
print("My python learning Jourey")

Salary = float(input("enter your Salary:"))

if Salary <= 10000:
    Tax = Salary * 5 / 100
elif Salary <= 30000:
    Tax = 10000 * 5 / 100 + (Salary - 10000) * 7 / 100
elif Salary <= 50000:
    Tax = 10000 * 5 / 100 + 30000 * 7 / 100 + (Salary - 30000) * 10 / 100
elif Salary <= 100000:
    Tax = 10000 * 5 / 100 + 30000 % 7 / 100 + 50000 % 10 / 100 + (Salary - 50000) * 12 / 100
else:
    Tax = 10000 * 5 / 100 + 30000 * 7 / 100 + 50000 * 10 / 100 + 100000 * 12 / 100 + (Salary - 100000) * 15 / 100


a = float(input("enter first nuber:"))
b = float(input("enter Second number:"))
Op = input("Operaters (+,-,*,/):")

if Op == "+":
    print("Result:", a + b)
elif Op == "-":
    print("Result:",a-b)
elif Op == "*":
    print("Result:", a*b)
elif Op == "/":
    print("Result:",a/b)
    if b == 0 :
        print("Error: zero se divide nhi ker Skta hai")
    else:
        print("Result:", a / b)
else:
    print("Operaters +,-,*,/")

