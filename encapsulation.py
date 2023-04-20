class Employee():
    def __init__(self):
        self.id = None
        # Write your code below
        self._id = 1

e = Employee()
print(dir(e))