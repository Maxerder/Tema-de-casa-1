#tema de casa 1

class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):#constructor
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):#destructor?
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status
   

#clasa mostenitoare
class Manager(Employee):
    mgrCount = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"E03_{department}
        Manager.mgrCount +=1

    def display_employee(self, display_option):#afisare info angajati
        if display_option % 3 ==0:
            print("Name: ", self.name)
        elif display_option % 3 ==1:
            print("Salary: ", self.salary)
        elif display_option % 3 ==2:
            print("Department: ", self.department)
    #SUPLIMENTAR
    

    

# Creați Y/3 obiecte ale clasei Manager
Y = 6  #Y=6 => 6/3=2 obiecte Manager
manager1 = Manager("Manager1", 5000, "1stTeam")
manager2 = Manager("Manager2", 6000, "2ndTeam")

# Apelați metoda ‘display_employee’ pentru obiectele din clasa Manager
for manager in [manager1, manager2]:
    manager.display_employee(0)  # Afisare nume angajat
    manager.display_employee(1)  # Afisare salariu angajat
    manager.display_employee(2)  # Afisare departament angajat

# Apelați metoda ‘display_employee’ pentru obiectele din clasa Employee
employee = Employee("Employee1", 4000)
employee.display_employee()

# Afișați valoarea atributului emp_count pentru o instanță a clasei Employee și pentru una a clasei Manager.
print(f"Employee Count: {employee.empCount}")   #employee

print(f"Manager Count: {manager1.mgrCount}")    #manager

#functii suplimentare 

def test_employee_class():
    employee = Employee("TestEmployee", 4500)
    if employee.name != "TestEmployee" or employee.salary != 4500 or employee.tasks != {}:
        print("Test failed: Initializarea corectă a obiectului Employee.")

    employee.update_salary(5000)
    if employee.salary != 5000:
        print("Test failed: Actualizarea salariului.")

    employee.modify_task("Task1", "InProgress")
    if employee.tasks["Task1"] != "InProgress":
        print("Test failed: Adăugarea și modificarea unei sarcini.")

    if Employee.empCount != 0:
        print("Test failed: Numărul de angajați nu a fost decrementat corect la ștergere.")
"""
print('\n')
def test_manager_class():
    #folosirea assert in loc de if
    #output.append
"""
test_employee_class()
#test_manager_class()
