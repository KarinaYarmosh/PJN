#Napisz program księgowy dla firmy.
# Zdefiniuj następujące obiekty:
# ●Employee (name, surname, salary)
# ●ReceivedInvoice(date, amount)
# ●IssuedInvoice(date, amount)
# Definicje klas umieść w module.
# Dane powinny być wczytywane z plików CSV
# (po jednym pliku CSV dla Employee,ReceivedInvoice, IssuedInvoice).
# Program powininen obliczyć budżet firmy (sumę wydatków i przychodów,
# bilans) dlakażdego miesiąca.
# Parsowanie daty:
# from datetime import datetime
# d = datetime.strptime('2018-06-05', '%Y-%m-%d')
# print(d.month)

class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

def str(self):
    return f"Employee: {self.name} {self.surname} {self.salary}"

class ReceivedInvoice:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

def str(self):
    return f"ReceivedInvoice: {self.date} {self.amount}"

class IssuedInvoice:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

def str(self):
    return f"IssuedInvoice: {self.date} {self.amount}"