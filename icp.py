class Employee:  # Employee class
    Num = 3

    def increment(self):
        self.__class__.Num += 1

    def __init__(self, name, family, salary, department):  # constructor
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

    def get_name(self):
        print("The employee's  name is :" + self.name)
        return

    def get_family(self):
        print("The employee's family is :" + self.family)
        return

    def get_salary(self):
        print("Employee's salary is : " + str(self.salary))
        return

    def get_salary_value(self):
        return self.salary

    def get_dept(self):
        print("Employee's department is : " + self.department)
        return

    def get_emp_num(self):
        print("Number of employees :" + str(self.Num))
        return


class FullTimeEmployee(Employee):  # inherited from class Employee
    def __init__(self, name, family, salary, department, workhours):
        Employee.__init__(self, name, family, salary, department)
        self.workhours = workhours

    def get_hours(self):
        print("Employee works for " + self.workhours + " hours")


def averagesalary():
    x = 0
    total = 0
    while x < len(eArray):
        total += eArray[x].get_salary_value()  # Salary + Total
        x += 1
    total = total / x
    print("The average salary is " + str(total))


# Creating Employees
Emp1 = Employee("hao", "A", 1000, "CS")
Emp2 = FullTimeEmployee("Zhang", "B", 2000, "EE", '8')
Emp3 = Employee("Chen", "C", 3000, "manger")
eArray = [Emp1, Emp2, Emp3]

print("Employee 1: ")
Emp1.get_name()
Emp1.get_family()
Emp1.get_salary()
Emp1.get_dept()
print("\n")
print("Employee 2: ")
Emp2.get_name()
Emp2.get_family()
Emp2.get_salary()
Emp2.get_dept()
Emp2.get_hours()
print("\n")

print("Employee 3: ")
Emp1.get_name()
Emp1.get_family()
Emp1.get_salary()
Emp1.get_dept()
print("\n")


Emp1.get_emp_num()
averagesalary()

