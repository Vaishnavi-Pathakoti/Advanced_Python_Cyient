from  dataclasses import dataclass
@dataclass
class Employee:
    employee_id: int
    employee_name: str
    department: str

employee=Employee(101,"Vaish", "Dev")
print(Employee)
print(employee.employee_name) 
print(employee.employee_id)   
print(employee.department)  