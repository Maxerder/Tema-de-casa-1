#tema de casa 1

class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
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
    #SUPLIMENTAR
    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)
    def sup_update_salary(self, new_salary):
        self.update_salary(new_salary)
        print(f"Updated salary: {self.salary}")
        print("Update salary test passed.\n")
    def sup_modify_task(self, task_name, status):
        self.modify_task(task_name, status)
        print(f"Modified tasks: {self.tasks}")
        print("Modify task test passed.\n")

#clasa mostenitoare
class Manager(Employee):
    mgrCount = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        Manager.mgrCount +=1

    def display_employee(self, display_option):#afisare info angajati
        if display_option==0:
            print("Name: ", self.name)
        elif display_option==1:
            print("Salary: ", self.salary)
        elif display_option==2:
            print("Department: ", self.department)
    

# Creați Y/3 obiecte ale clasei Manager
Y = 6  #Y=6 => 6/3=2 obiecte Manager
manager1 = Manager("Manager1", 5000, "IT Department")
manager2 = Manager("Manager2", 6000, "HR Department")

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

def suplimentar():
    #Crearea unui obiect Employee
    sup_employee = Employee("supEmployee", 3000)

    #Teste pentru Employee
    sup_employee.sup_update_salary(3500)
    sup_employee.sup_modify_task("New Task Sup","New Sup")

suplimentar()