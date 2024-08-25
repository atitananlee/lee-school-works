class Employee :
    _minnimum=85000
    _maximum=250000
    companame='leeling lins .co'
    def __init__(self,name,salary,department):
        self._name = name
        self._salary = salary
        self._department = department
    def _showdata(self):
        print('name = {}'.format(self._name))
        print('salary = {}'.format(self._salary))
        print('department = {}'.format(self._department))
    def _income(self):
        return self._salary*12
    def __str__(self):
        return('Employee name = , department = ,Salary ='.format(self._name,self._salary,self._department))'

class Accountting(Employee):
    _departmentname='Accountting'
    def __init__(self, name, salary, department):
        super().__init__(name, salary,self._departmentname)
        self._age = age
    def _showdata(self):
        super()._showdata()
        print*('age = '+str(self._age))

    account = Accountting('next',10000,30)
    account._showdata()
    