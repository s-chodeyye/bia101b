#the below codes calculates the tax based on the annual income of the taxpayer.

class Taxpayer: #parentclass
    def __init__(self, name, id, salary, deductions):
        self.name = name
        self.id = id
        self.salary = salary
        self.deductions = deductions

    def calculate_gross_income(self):#returns the gross income(salary)
        return self.salary

    def calculate_deductions(self): #calculates total deductions by summing up the values in the deductions dictionary
        return sum(self.deductions.values())

    def calculate_net_income(self): #returns net income  by substracting total deductions from gross income.
        return self.calculate_gross_income() - self.calculate_deductions()

    def calculate_tax_from_slabs(self, income): #calculates the tax based on different income slabs. surcharge is added if the tax exceeds nu 1,000,000.
        if income <= 300000:
            return 0
        elif income <= 400000:
            return (income - 300000) * 0.1
        elif income <= 650000:
            return 10000 + (income - 400000) * 0.15
        elif income <= 1000000:
            return 47500 + (income - 650000) * 0.2
        elif income <= 1500000:
            return 117500 + (income - 1000000) * 0.25
        else:
            tax = 242500 + (income - 1500000) * 0.3
            # Surcharge if PIT is equal to or more than Nu. 1,000,000
            if tax >= 1000000:
                tax += tax * 0.1
            return tax

    def calculate_tax(self):#calculates tax based on the net income.
        net_income = self.calculate_net_income()
        return self.calculate_tax_from_slabs(net_income)

class RegularEmployee(Taxpayer):#inherits from taxpayer
    def __init__(self, name, id, salary, deductions, organization_type):
        super().__init__(name, id, salary, deductions)
        self.organization_type = organization_type

    def calculate_deductions(self):#here it will include additional deductions(NPPF and GIS) for corporate/private employees).
        deductions = super().calculate_deductions()
        if self.organization_type in ['Corporate', 'Private']:
            # NPPF and GIS applicable for regular employees in Corporate/Private
            deductions += self.deductions.get('NPPF', 0)
            deductions += self.deductions.get('GIS', 0)
        return deductions

class ContractEmployee(Taxpayer):#here also it inherits from the parent class i.e, Taxpayer
    def __init__(self, name, id, salary, deductions):
        super().__init__(name, id, salary, deductions)

    def calculate_deductions(self):
        # Contract employees typically do not have NPPF or GIS
        return super().calculate_deductions()

# Example usage
def main():
    # Define some deductions
    deductions_regular = { #a dicyionary of typical deductions for regular employees, including education allowance, life insurance, self education, donations, NPPF, and GIS.
        'education_allowance': 350000,
        'life_insurance': 100000,
        'self_education': 150000,
        'donations': 50000,
        'NPPF': 50000,
        'GIS': 20000
    }

    deductions_contract = { #a dictionary of typical deductions for contract employees, excluding NPPF and GIS
        'education_allowance': 350000,
        'life_insurance': 100000,
        'self_education': 150000,
        'donations': 50000
    }

    # Create instances for regular and contract employees
    regular_employee1 = RegularEmployee(name="sonam", id="106002131078", salary=1200000, deductions=deductions_regular, organization_type="Corporate")
    regular_employee2= RegularEmployee(name="pema", id="106002131034", salary=1850000, deductions=deductions_regular, organization_type="Corporate")
    regular_employee3 = RegularEmployee(name="zangmo", id="106002137864", salary=180000, deductions=deductions_regular, organization_type="Corporate")
    regular_employee4= RegularEmployee(name="selden", id="106002780378", salary=2000000, deductions=deductions_regular, organization_type="Corporate")
    regular_employee5= RegularEmployee(name="dorji", id="106002092576", salary=650000, deductions=deductions_regular, organization_type="Corporate")
    contract_employee1 = ContractEmployee(name="choden", id="10803001026", salary=8000000, deductions=deductions_contract)
    contract_employee2= ContractEmployee(name="chophel", id="10803008976", salary=180000, deductions=deductions_contract)
    contract_employee3= ContractEmployee(name="choying", id="10803897654", salary=1600100, deductions=deductions_contract)
    contract_employee4= ContractEmployee(name="samphel", id="10890874563", salary=2000000, deductions=deductions_contract)
    contract_employee5= ContractEmployee(name="dophu", id="10803008967", salary=1850000, deductions=deductions_contract)
    
    # Calculate tax for each regular employee and prints the results using isinstance to ensure the tax calculation returned a valid number.
    total_tax_regular = regular_employee1.calculate_tax()
    if isinstance(total_tax_regular, (int, float)):
        print(f"Total tax payable by {regular_employee1.name}: Nu. {total_tax_regular:.2f}")
    else:
        print(f"Error calculating tax for {regular_employee1.name}")

    total_tax_regular = regular_employee2.calculate_tax()
    if isinstance(total_tax_regular, (int, float)):
        print(f"Total tax payable by {regular_employee2.name}: Nu. {total_tax_regular:.2f}")
    else:
        print(f"Error calculating tax for {regular_employee2.name}")
    
    total_tax_regular = regular_employee3.calculate_tax()
    if isinstance(total_tax_regular, (int, float)):
        print(f"Total tax payable by {regular_employee3.name}: Nu. {total_tax_regular:.2f}")
    else:
        print(f"Error calculating tax for {regular_employee3.name}")
    
    total_tax_regular = regular_employee4.calculate_tax()
    if isinstance(total_tax_regular, (int, float)):
        print(f"Total tax payable by {regular_employee4.name}: Nu. {total_tax_regular:.2f}")
    else:
        print(f"Error calculating tax for {regular_employee4.name}")
    
    total_tax_regular = regular_employee4.calculate_tax()
    if isinstance(total_tax_regular, (int, float)):
        print(f"Total tax payable by {regular_employee5.name}: Nu. {total_tax_regular:.2f}")
    else:
        print(f"Error calculating tax for {regular_employee5.name}")

    # Calculate tax for each contract employee and prints the results using isinstance to ensure the tax calculation returned a valid number.
    total_tax_contract = contract_employee1.calculate_tax()
    if isinstance(total_tax_contract, (int, float)):
        print(f"Total tax payable by {contract_employee1.name}: Nu. {total_tax_contract:.2f}")
    else:
        print(f"Error calculating tax for {contract_employee1.name}")

    total_tax_contract = contract_employee2.calculate_tax()
    if isinstance(total_tax_contract, (int, float)):
        print(f"Total tax payable by {contract_employee2.name}: Nu. {total_tax_contract:.2f}")
    else:
        print(f"Error calculating tax for {contract_employee2.name}")
    
    total_tax_contract = contract_employee3.calculate_tax()
    if isinstance(total_tax_contract, (int, float)):
        print(f"Total tax payable by {contract_employee3.name}: Nu. {total_tax_contract:.2f}")
    else:
        print(f"Error calculating tax for {contract_employee3.name}")

    total_tax_contract = contract_employee4.calculate_tax()
    if isinstance(total_tax_contract, (int, float)):
        print(f"Total tax payable by {contract_employee4.name}: Nu. {total_tax_contract:.2f}")
    else:
        print(f"Error calculating tax for {contract_employee4.name}")

    total_tax_contract = contract_employee5.calculate_tax()
    if isinstance(total_tax_contract, (int, float)):
        print(f"Total tax payable by {contract_employee5.name}: Nu. {total_tax_contract:.2f}")
    else:
        print(f"Error calculating tax for {contract_employee5.name}")
    # Interactive part for user input, it allows user input to dynamically create an employee and calculate their tax.
    name = input("Enter your name: ")
    id = input("Enter your ID: ")
    salary = float(input("Enter your salary: "))
    employment_type = input("Enter your employment type (Regular/Contract): ")
    
    # Define some deductions based on user input.
    deductions = {
        'education_allowance': float(input("Enter your education allowance: ")),
        'life_insurance': float(input("Enter your life insurance: ")),
        'self_education': float(input("Enter your self education: ")),
        'donations': float(input("Enter your donations: "))
    }
    #create an employee based on the type of employment
    if employment_type.lower() == "regular":
        organization_type = input("Enter your organization type (Corporate/Private/Other): ")
        deductions['NPPF'] = float(input("Enter your NPPF: "))
        deductions['GIS'] = float(input("Enter your GIS: "))
        employee = RegularEmployee(name, id, salary, deductions, organization_type)
    else:
        employee = ContractEmployee(name, id, salary, deductions)
    #calculate and print the tax for the user
    total_tax = employee.calculate_tax()
    if isinstance(total_tax, (int, float)):
        print(f"Total tax payable by {employee.name}: Nu. {total_tax:.2f}")
    else:
        print(f"Error calculating tax for {employee.name}")



main()

#To summarize
# the code specifies a tax computation mechanism for two sorts of employees: regular and contract. 
#It has classes for each category, which derive from a base 'Taxpayer' class.
# Each class computes gross income, deductions, net income, and tax using preset slabs.
# Certain organizational kinds (corporate/private) are eligible for additional deductions under the 'RegularEmployee' class. 
#In the main function, numerous instances of 'RegularEmployee' and 'ContractEmployee' are created with predefined data and their tax calculations are printed. 
#The code also includes an interactive part in which users can enter their own information to dynamically generate an employee object and calculate their tax.
#Key Functionalities: 
#1. Taxpayer Class: Base class that includes methods for calculating income and taxes. 
#2. RegularEmployee Class: Expands 'Taxpayer' to include specified deductions. 
#3. ContractEmployee Class: Extends 'Taxpayer' without any further deductions. 
#4. Primary Function: Generates employee instances, calculates, and prints taxes. 
#5. Interactive Section: Accepts user input to calculate and print tax for custom employee information.
# This solution provides for flexible and precise tax estimates based on employee type and available deductions.
