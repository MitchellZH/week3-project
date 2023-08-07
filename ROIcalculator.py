class ROI():
    def __init__(self):
        self.monthly_income = 0.0
        self.monthly_expenses = 0.0
        self.monthly_cash_flow = 0.0
        self.total_investment = 0.0
        self.annual_cash_flow = 0.0
        self.cash_on_cash = 0.0

    def calculate_income(self):
        print("Please enter how much monthly income you get from each resource below")
        rental = input("Rental: ")
        laundry = input("Laundry: ")
        storage = input("Storage: ")
        misc = input("Misc: ")
        self.monthly_income = float(rental) + float(laundry) + float(storage) + float(misc)
        print(f"Your total monthly income is {self.monthly_income}")
    
    def calculate_expenses(self):
        print("How much do you pay monthly of each expense below")
        tax = input("Tax: ")
        insurance = input("Insurance: ")
        utilities = input("Utilities: ")
        hoa = input("HOA: ")
        lawn_or_snow = input("Lawn/Snow: ")
        vacancy = input("Vacancy: ")
        repairs = input("Repairs: ")
        cap_ex = input("Capital Expenditures: ")
        prop_management = input("Property Management: ")
        mortgage = input("Mortgage: ")
        self.monthly_expenses = float(tax) + float(insurance) + float(utilities) + float(hoa) + float(lawn_or_snow) + float(vacancy) + float(repairs) + float(cap_ex) + float(prop_management) + float(mortgage)
        print(f"Your total monthly expenses are {self.monthly_expenses}")
    
    def calculate_cash_flow(self):
        self.monthly_cash_flow = self.monthly_income - self.monthly_expenses
        print(f"Your Total Monthly Cash Flow based on your above answers is {self.monthly_cash_flow}")
    
    def calculate_roi(self):
        print("How much did you invest in each cost below")
        down_payment = float(input("Down Payment: "))
        closing_costs = float(input("Closing costs: "))
        rehab_budget = float(input("Rehab Budget: "))
        misc = float(input("Misc: "))
        self.total_investment = down_payment + closing_costs + rehab_budget + misc
        print(f"Your Total Investment Costs were {self.total_investment}")
        self.annual_cash_flow = self.monthly_cash_flow * 12
        print(f"Your Total Annual Cash Flow is {self.annual_cash_flow}")
        self.cash_on_cash = (self.annual_cash_flow/self.total_investment)*100
    
    def runner(self):
        print("Welcome to the ROI Calculator")
        self.calculate_income()
        self.calculate_expenses()
        self.calculate_cash_flow()
        self.calculate_roi()
        print("Based on our calculations")
        return print(f"Your ROI is {self.cash_on_cash}%")
    
roi_calculator = ROI()

roi_calculator.runner()
    