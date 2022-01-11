#QUESTION 2
gross = int(input("Enter the gross income:- "))
num_Dependent = int(input("Enter the number of dependents:- "))

Tax_Income = gross - 10000 - (3000 * num_Dependent)

Tax = Tax_Income * (0.4)

print(Tax)