'''” нас есть численные данные из разных источников. 
≈сли они в виде строк, то нужно привести их к числам, 
а пропуски Ч заполнить значени€ми. 
—делаем доступ к медиане, среднему значению и стандартному отклонению.
¬ __init__ мы использовали значение по умолчанию дл€ fill_value, 
а методы позвол€ют нам определ€ть необ€зательные параметры.'''

import statistics  
  
class DataFrame():  
    def __init__(self, column, fill_value=0):  
        # »нициализируем атрибуты  
        self.column = column  
        self.fill_value = fill_value  
        # «аполним пропуски  
        self.fill_missed()  
        #  онвертируем все элементы в числа  
        self.to_float()  
          
    def fill_missed(self):  
        for i, value in enumerate(self.column):  
            if value is None or value == '':  
                self.column[i] = self.fill_value  
                  
    def to_float(self):  
        self.column = [float(value) for value in self.column]  
      
    def median(self):  
        return statistics.median(self.column)  
      
    def mean(self):  
        return statistics.mean(self.column)  
      
    def deviation(self):  
        return statistics.stdev(self.column)  
      
  
      
# ¬оспользуемс€ классом  
df = DataFrame(["1", 17, 4, None, 8])  
  
print(df.column)  
# => [1.0, 17.0, 4.0, 0.0, 8.0]  
print(df.deviation())  
# => 6.89  
print(df.median())  
# => 4.0  





