from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = AbstractEmployee.new_id

        AbstractEmployee.new_id += 1
        
    @abstractmethod
    def say_id(self) -> str:
        return f'My id is: {self.id}'


class User():
    def __init__(self, username: str):
        self.username = username


class Company():
    Company_employees: list = []

    def __init__(self, name: str = 'NotDefined', field: str = 'NotDefined'):
        self.name = name
        self.field = field


    def __len__(self) -> int:
        return len(self.Company_employees)
    
    def __name__(self) -> str:
        return self.name

    def Add_employee(self, employee: str) -> list:
        self.Company_employees.append(employee)


class Meeting():
    meeting_status: bool = False

    def __init__(self, company) -> None:
        self.company = company

    def Meeting_list(self) -> str:
        print(f'Meeting members: {len(Company.Company_employees)}')

    def Meeting_status(self) -> str:
        return Meeting.meeting_status
    
    def Create_meeting(self) -> str:
        Meeting.meeting_status = True
        print(f'Meeting started! hosted by: {self.company.name}')

    def Host(self) -> str:
        print(f'Hosted by: {self.company.name}')

    def Close_Meeting(self) -> str:
        Meeting.meeting_status = False
        print('Meeting closed!')


class Employee(AbstractEmployee, User):
    def __init__(self, name: str, username: str):
        super().__init__(self)
        User.__init__(self, username)
        
        self.name = name
        self.username = username
        self.role = 'Employee'

    def say_id(self) -> str:
        print(f'My id is: {self.id}, and my role is: {self.role}')

    def say_name(self) -> str:
        print(f'My name is: {self.name}!')


class Admin(Employee):
    def __init__(self, name: str, username: str):
        super().__init__(name, username)

        self.name = name
        self.username = username
        self.role = 'Admin'



if __name__ == '__main__':

    company1 = Company('CELPE', 'Energia')

    joao = Employee('joao', 'coringa37')
    adm = Admin('adm', 'useradm')

    meeting1 = Meeting(company1)

    company1.Add_employee(joao)

    joao.say_name()
    joao.say_id()

    adm.say_name()
    adm.say_id()

    meeting1.Host()