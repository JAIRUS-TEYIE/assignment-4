class Employee:
    def __init__(self, name, employeeId, baseSalary):
        self.name = name
        self.employeeId = employeeId
        self.baseSalary = baseSalary
    def __str__(self):
        return f"\nName: {self.name},\nID: {self.employeeId},\nBase Salary: Kshs. {self.baseSalary},\n"
    def calculateSalary(self):
        return self.baseSalary

class FullTimeEmployee(Employee):
    def __init__(self, name, employeeId,baseSalary, benefits):
        super().__init__(name, employeeId, baseSalary)
        self.benefits = benefits
    def __str__(self):
        return super().__str__() + f"Benefits: {self.benefits}\n"
    def calculateSalary(self):
        return self.baseSalary + self.benefits
      

class PartTimeEmployee(Employee):
    def __init__(self, name, employeeId, hourlyRate, hoursWorked):
        baseSalary = hourlyRate * hoursWorked
        super().__init__(name, employeeId, baseSalary)
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked
    def __str__(self):
        return (super().__str__() + f"Hourly Rate: {self.hourlyRate}, Hours Worked: {self.hoursWorked}\n")
    def calculateSalary(self):
        return self.hourlyRate * self.hoursWorked

class Company:
    def __init__(self):
        self.employees = []
    def addEmployee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")
    def displayEmployees(self):
        if not self.employees:
            print("No employees to display.")
        else:
            for employee in self.employees:
             print(employee)
    def calculateTotalSalary(self):
            totalSalary = sum(employee.calculateSalary() for employee in self.employees)
            print(f"\nTOTAL SALARY EXPENSE: KSHS. {totalSalary}")

if __name__ == '__main__':
    company = Company()
#Adding Employees
company.addEmployee(FullTimeEmployee ('Jairus Teyie', 5433, 8500, 3000))
company.addEmployee(FullTimeEmployee ('Ellemina Kavita', 2137, 6300, 2200))
company.addEmployee(FullTimeEmployee ('Godwil Kihima', 1904, 6000, 2000))
company.addEmployee(PartTimeEmployee ('Esther Lozenja', 8165, 10, 40))
company.addEmployee(PartTimeEmployee ('Elizabeth Nasmiyu', 6715, 13, 35))
company.displayEmployees() #Display Employees
# Calculate total salary expense
company.calculateTotalSalary()

