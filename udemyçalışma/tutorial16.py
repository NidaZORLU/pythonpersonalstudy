from abc import ABC

class Tax_paying(ABC):

    salary = 0

    def calculate_tax_value(self):
        pass

class StudentTaxPaying(Tax_paying):

    def __init__(self, salary):
        self.salary = salary

    def calculate_tax_value(self):
       self.tax_value = 0
       tax_value = (self.salary * 15)/100
       return tax_value


class WorkerTaxPaying(Tax_paying):

    def __init__(self, salary):
        self.salary = salary

    def calculate_tax_value(self):
        self.tax_value = 0

        if self.salary <= 80000:
            tax_value = (self.salary * 17)/100
            return tax_value

        else:
            tax_value = ((self.salary * 18)/100)+((self.salary-80000) * 32)/100
            return tax_value


class DisableTaxPaying(Tax_paying):

    def __init__(self, salary):
        self.salary = salary

    def calculate_tax_value(self):
       self.tax_value = 0
       tax_value= (self.salary*12)/100
       return tax_value

tax_student = StudentTaxPaying(50000)
tax_disable = DisableTaxPaying(70000)
tax_worker1 = WorkerTaxPaying(68000)
tax_worker2 = WorkerTaxPaying(120000)


tax_payers = [tax_student, tax_disable, tax_worker1, tax_worker2]

for i in tax_payers:
   print(i.calculate_tax_value())
