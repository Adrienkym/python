class User():

    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        

    def display_info(self):
        print(f"Name: {self.name}")

    def print_details(self):
        print("-----------------")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print("-----------------")



class Employee(User):
    def __init__(self, name, email, phone, password, salary):
        super().__init__(name, email, phone, password)
        self.salary = salary
    def print_details(self):
        super().print_details()
        print(f"Salary: {self.salary}")
        print("-----------------")  

class Customer(User):
    def __init__(self, name, email, phone, password, address):
        super().__init__(name, email, phone, password)
        self.address = address   
    def print_details(self):
        super().print_details()
        print(f"Address: {self.address}")
        print("-----------------")   

emp1 = Employee(name="John Doe", email="john@jhn", phone="1234567890", password="pass123", salary=50000)
cust1 = Customer(name="Jane Smith", email="jane@jhn", phone="0987654321", password="pass456", address="123 Main St")

emp1.print_details()
cust1.print_details()
        
