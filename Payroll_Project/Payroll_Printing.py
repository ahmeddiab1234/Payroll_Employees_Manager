from abc import ABC, abstractmethod
# from Employees import Employee as EMP
from Validations import *
from Invoices_Payroll import Employee, Invoice

class ShowEmployees:
    @staticmethod
    def _show(emp_lst):
        emp_lst = sorted(emp_lst, key= lambda x: (x.name, x.salary))
        print('Class Name \t\t Employee Name \t\t Employee Address')
        for emp in emp_lst:
            print(f'{emp.__class__.__name__} \t\t {emp.name} \t\t {emp.address}')
        print()


class ShowInvoices:
    @staticmethod
    def _show(inv_lst):
        inv_lst = sorted(inv_lst, key= lambda x: (x.name, x.invoice_id))
        print('Class Name \t\t Invoice Name \t\t Invoice Address')
        for inv in inv_lst:
            print(f'{inv.__class__.__name__} \t\t {inv.name} \t\t {inv.invoice_id}')
        print()



if __name__ == '__main__':
    employee1 = Employee('ahmed', 'Egypt Sharqia',5000)
    employee2 = Employee('mohammed', 'Egypt Cairo', 7000)

    invoice1 = Invoice('Sayed', '111')
    invoice2 = Invoice('hesham', '112')

    employee3 = Employee('diab', 'Egypt cairo',8000)
    employee4 = Employee('nagy', 'USA Stanford', 6340)

    invoice3 = Invoice('reyad', '113')
    invoice4 = Invoice('ashraf', '114')

    employee_lst = [employee1, employee2, employee3, employee4]
    invoice_lst = [invoice1, invoice2, invoice3, invoice4]

    ShowEmployees()._show(employee_lst)
    ShowInvoices()._show(invoice_lst)

