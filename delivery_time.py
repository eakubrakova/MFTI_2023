dish_time_dict = {
    '����� � ���������': 15,
    '����': 18,
    '������ � �������': 20,
    '������ � ���������': 24,
    '���� � �������': 28
}

street_time_dict  = {
    '�����������': 39,
    '���������': 40,
    '���������': 27,
    '�����������': 43,
    '���������': 37,
    '�����������': 34
}

dish, street = '����� � ���������', '���������'



if street not in street_time_dict: 
    # ����������� �����
    print("�������� � ��� ����� ����������")
elif dish not in dish_time_dict:
    # ����������� �����
    print("����� ����������, �������� ���-�� ������") 
else: 
    # ����� �������� ��� �������� � ����� ��������
    dish_time = dish_time_dict[dish] # ����� ������������� �����
    street_time = street_time_dict[street] # ����� ��������
    full_time = dish_time + street_time  # ����� ����� ��������
    delay = full_time - 60  # ��������
    if delay <= 0: 
        # �������� �� ������������
        print("����� ����� ��������� �������")
    else:  
        # �������� �������������
        print("������ ���������� �� {} �����".format(delay))