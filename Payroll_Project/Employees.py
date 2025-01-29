class Worker:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address


class Employee(Worker):
    def __init__(self, name, address, job_title,monthly_salary, salary_type='Monthly', commission=0, hourly_salary=None,  project_salary=None, num_hours=8):
        super().__init__(name, address)
        self.job_title = job_title
        self.salary_type = salary_type
        self.commission = commission
        self.hourly_salary = hourly_salary
        self.monthly_salary = monthly_salary
        self.project_salary = project_salary
        self.num_hours = num_hours

    def get_salary(self):
        if self.salary_type == 'Monthly':
            return self.monthly_salary
        elif self.salary_type == 'Hourly':
            return self.hourly_salary * self.num_hours
        elif self.salary_type == 'Project Salary':
            return self.project_salary
        else:
            return 0

    def get_total_salary(self):
        total_salary = self.get_salary()
        if self.commission:
            total_salary += total_salary * self.commission
        return total_salary

    def change_salary(self, salary_type, salary_amount):
        self.salary_type = salary_type
        if salary_type == 'Monthly':
            self.monthly_salary = salary_amount
        elif salary_type == 'Hourly':
            self.hourly_salary = salary_amount
        elif salary_type == 'Project Salary':
            self.project_salary = salary_amount

    def change_job(self, new_job_title, new_salary):
        self.job_title = new_job_title
        self.monthly_salary = new_salary
        return new_job_title, new_salary


class Volunteer(Worker):
    def __init__(self, name, address, job_title, salary=0, rewards=0, num_hours=0, organization=None):
        super().__init__(name, address)
        self.job_title = job_title
        self.salary = salary
        self.rewards = rewards
        self.num_hours = num_hours
        self.organization = organization

    def get_total_salary(self):
        total_salary = self.salary
        if self.rewards:
            total_salary += self.rewards
        return total_salary

    def change_organization(self, organization):
        self.organization = organization

    def change_job(self, new_job_title, new_organization):
        self.job_title = new_job_title
        self.organization = new_organization
        return new_job_title, new_organization


if __name__ == '__main__':

    employee = Employee("John Doe", "123 Main St", "Software Engineer", monthly_salary=5000, salary_type='Monthly')
    print(f"Employee Total Salary: {employee.get_total_salary()}")

    volunteer = Volunteer("Jane Doe", "456 Elm St", "Community Helper", salary=0, rewards=100, organization="Green Earth")
    print(f"Volunteer Total Salary: {volunteer.get_total_salary()}")

