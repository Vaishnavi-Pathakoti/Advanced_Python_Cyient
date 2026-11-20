class invalidSalaryError(Exception):
    pass
def calculate(salary):
    if salary <= 0:
        raise invalidSalaryError("salary must be greater than 0")
    print("Employee Salary")

try:
    calculate(-500)

except invalidSalaryError as error:
    print("Error: ", error)