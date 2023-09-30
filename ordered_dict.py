from collections import OrderedDict

def check(temps):
    # ���������� ������ temps �� ������� �������� ������� �������
    sorted_temps = sorted(temps, key=lambda x: x[1], reverse=True)
    
    # �������� ������� � ���������������� ����������
    result = OrderedDict(sorted_temps)
    
    # ����� �������
    print(result)

# ������ ������ temps
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

# ����� ������� check
check(temps)
