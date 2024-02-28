class Employee:
    def __init__(self, eid, name, dept,
                 gender, salary, desig):
        self.setEmp(eid, name, dept,
                    gender, salary, desig)
    def setEmp(self, eid, name, dept,
                gender, salary, desig):
        self.id = eid
        self.name = name
        self.dept = dept
        self.salary = salary
        self.gender = gender
        self.desig = desig
        
    def showEmp(self):
        print("""
Employee id : %d
Name        : %S
Department  : %S
Gender      : %S
Salary      : %S
Designation : %S
""" % (self.id, self.name, self.dept,
       self.gender, self.salary, self.desig))

    def calcSalary(self):
        self.final_salary = (0.05 * self.salary +\
                             0.03 * self.salary) -\
                             0.08 * self.salary
        print("Final salary is : ", self.salary)

    def isBonus(self):
      return self.salary < 30,000

david = Employee(100, "David", "Accounting", 'M', 25000, "Manager")
ravi = Employee(101, "Ravi", "Marketing", 'M', 30000, "Clerk")
david.calcSalary()
ravi.calcSalary()

if david.isBonus():
  print("David is eligible for bonus")
else:
  print("David is not eligible for bonus")
