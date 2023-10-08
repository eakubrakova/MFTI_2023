class SalesReport():  
    def __init__(self, employee_name):  
        self.deals = []  
        self.employee_name = employee_name  
      
    def add_deal(self, company, amount):   
        self.deals.append({'company': company, 'amount': amount})  
          
    def total_amount(self):  
        return sum([deal['amount'] for deal in self.deals])  
      
    def average_deal(self):  
        return self.total_amount()/len(self.deals)  
      
    def all_companies(self):  
        return list(set([deal['company'] for deal in self.deals]))  
      
    def print_report(self):  
        print("Employee: ", self.employee_name)  
        print("Total sales:", self.total_amount())  
        print("Average sales:", self.average_deal())  
        print("Companies:", self.all_companies())  
      
      
report = SalesReport("Ivan Semenov")  
  
report.add_deal("PepsiCo", 120_000)  
report.add_deal("SkyEng", 250_000)  
report.add_deal("PepsiCo", 20_000)  
  
report.print_report()  
# => Employee:  Ivan Semenov  
# Total sales: 390000  
# Average sales: 130000.0  
# Companies: ['PepsiCo', 'SkyEng'] 
