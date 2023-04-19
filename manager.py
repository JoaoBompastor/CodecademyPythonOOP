class Employee():
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f'My id is: {self.id}')


# Write your code below
class Admin(Employee): 
    def say_id(self):
        super().say_id()
        print('I am an Admin')


# Write your code below
class Manager(Admin):
    def say_id(self):
        print('I am in Charge!')
        super().say_id()


e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()

# e1.say_id()
# e2.say_id()
# e3.say_id()
e4.say_id()