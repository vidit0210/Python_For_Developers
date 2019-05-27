class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def get_name(self):
        return '{} {}'.format(self.fname, self.lname)


class Programmer(Employee):
    def __init__(self, fname, lname, salary, programming_language):
        super().__init__(fname, lname, salary)
        self.programming_language = programming_language


p1 = Programmer('Vidit', 'Shah', '100K', 'python')
