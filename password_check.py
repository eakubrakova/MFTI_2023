errors_dict = {
    'length': '����� ������ �� ����� 8 ��������',
    'digits': '������ ������� ������ �� ����',
    'letters': '������ ������� ������ �� ����',
    'upper': '����������� ��������� �����',
    'lower': '����������� �������� �����',
    'spec': '����������� ����������� � ������',
    'bad_symbols': '� ������ ������������ ����������������� �������'
}

bad_symbols = ['!', '@', '$', '%', '^', '`', '&', '(', ')', '+', '=', '_', '~']
password = 'Aafaf*al'

# ��������� ����� ������
if len(password) == 8:
    errors_dict.pop('length')

# ���������, ��� ������ �� ������� ������ �� ����
if not password.isdigit():
    errors_dict.pop('digits')

# ���������, ��� ������ �� ������� ������ �� ����
if not password.isalpha():
    errors_dict.pop('letters')

# ���������, ���� �� � ������ ��������� �����
if password.lower() != password:
    errors_dict.pop('upper')

# ���������, ���� �� � ������ �������� �����
if password.upper() != password:
    errors_dict.pop('lower')

# ���������, ���� �� � ������ ����������� �������
if '*' in password or '-' in password or '#' in password:
    errors_dict.pop('spec')
    # ���������, ����������� �� ���� ������� � ������ ��������� ���
    if password.count('*') > 1 or password.count('-') > 1 or password.count('#') > 1:
        errors_dict['spec_count'] = '�����-�� �� ������������ � ������ ����������� ����� ������ ����'

# ���������, ���� �� � ������ ����������� �������
if len(set(password).intersection(set(bad_symbols))) == 0:
    errors_dict.pop('bad_symbols')

# ��������� �������������� ����� ���-�����
if len(errors_dict) > 0:
    print(list(errors_dict.values()))
else:
    print('������ �������!')
