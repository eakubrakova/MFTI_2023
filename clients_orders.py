class Client():  
    # ������� ������  
    def __init__(self, email, order_num, registration_year):  
        self.email = email  
        self.order_num = order_num  
        self.registration_year = registration_year  
        self.discount = 0  
          
    # ���������� ������  
    def make_order(self, price):  
        self.update_discount()  
        self.order_num += 1  
        # ����� ���� �� ���������� ������, �� �� ������ ������� ��� ����  
        discounted_price = price * (1 - self.discount)   
        print(f"Order price for {self.email} is {discounted_price}")  
              
    # ���������� ������  
    def update_discount(self):   
        if self.registration_year < 2018 and self.order_num >= 5:  
            self.discount = 0.1   
              
  
# ����������  
          
# ������� ������� ����  
client_db = [   
    Client("max@gmail.com", 2, 2019),  
    Client("lova@yandex.ru", 10, 2015),  
    Client("german@sberbank.ru", 4, 2017)  
]  
  
  
# ����������� ������  
client_db[0].make_order(100)  
# => Order price for max@gmail.com is 100  
  
client_db[1].make_order(200)  
# => Order price for lova@yandex.ru is 180.0  
  
client_db[2].make_order(500)  
# => Order price for german@sberbank.ru is 500  
  
client_db[2].make_order(500)  
# => Order price for german@sberbank.ru is 450.0 
