import datetime

class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title
        self.date_hired = ""

class Company:
    def __init__(self, name, industry, address):
        self.name = name
        self.industry = industry
        self.address = address
        self.employees = []

    def hire(self, employee):
        employee.date_hired = datetime.date.today()
        self.employees.append(employee)

    def list_employees(self):
        print(f"{self.name} is in the {self.industry} industry and has the following employees")
        for employee in self.employees:
            print(f"* {employee.name}")

apple = Company("Apple", "Mac", "123 apple blvd")
microsoft = Company("Microsoft", "PC", "123 surface st")

matt = Employee("Matthew Kroeger", "programmer")
mike = Employee("Mike Prince", "programmer")
cooper = Employee("Cooper Nichols", "programmer")
katie = Employee("Katie Wohl", "programmer")
roxy = Employee("Frogxanne", "programmer")

microsoft.hire(matt)
microsoft.hire(mike)
apple.hire(cooper)
apple.hire(katie)
apple.hire(roxy)

apple.list_employees()
microsoft.list_employees()