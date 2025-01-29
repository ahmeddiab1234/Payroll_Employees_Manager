class Item:
    def __init__(self, description, quantity, price_per_item):
        self.description = description
        self.quantity = quantity
        self.price_per_item = price_per_item

    def total_price(self):
        return self.quantity * self.price_per_item


class Invoice:
    def __init__(self, name, invoice_id):
        self.name = name
        self.invoice_id = invoice_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_invoice_price(self):
        return sum(item.total_price() for item in self.items)


class Payable:
    def __init__(self, name):
        self.name = name

    def amount_to_pay(self):
        raise NotImplementedError("Subclasses must implement this method")


class Employee(Payable):
    def __init__(self, name, salary, address):
        super().__init__(name)
        self.salary = salary
        self.address = address

    def amount_to_pay(self):
        return self.salary


class InvoicePayable(Payable):
    def __init__(self, name, invoice):
        super().__init__(name)
        self.invoice = invoice

    def amount_to_pay(self):
        return self.invoice.total_invoice_price()


class Company:
    def __init__(self):
        self.payables = []

    def add_payable(self, payable):
        self.payables.append(payable)

    def total_paid_money(self):
        return sum(payable.amount_to_pay() for payable in self.payables)

    def print_payroll(self):
        print("Payroll Summary:")
        for payable in self.payables:
            print(f"{payable.name}: ${payable.amount_to_pay()}")
        print(f"Total Paid Money: ${self.total_paid_money()}")


if __name__ == "__main__":
    item1 = Item("Book: Python Programming", 2, 50)
    item2 = Item("Food: Organic Apples", 5, 3)

    invoice = Invoice('ahmed', "111")
    invoice.add_item(item1)
    invoice.add_item(item2)

    employee1 = Employee("John Doe", 5000, 'Egypt Sharqia')
    employee2 = Employee("Jane Smith", 6000, 'Egypt Mansora')
    invoice_payable = InvoicePayable("Supplier XYZ", invoice)

    company = Company()
    company.add_payable(employee1)
    company.add_payable(employee2)
    company.add_payable(invoice_payable)

    company.print_payroll()


    
"""

Let's extend the system
● There are invoices: each invoice has set of items (e.g. books, food, etc)
○ Each item has description, total quantity and price per item
○ Each item has its own details (e.g. book author name)
○ Invoice price: sum of the items prices
● The payroll consists of a payables list
○ Each payable is either employee or invoice
○ The total paid money is the total paid money for the added employees and invoices
● Create class Company
○ It creates several types of payables, add to Payroll and compute total paid money

"""
