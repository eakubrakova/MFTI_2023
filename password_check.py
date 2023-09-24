errors_dict = {
    'length': 'Длина пароля не равна 8 символам',
    'digits': 'Пароль состоит только из цифр',
    'letters': 'Пароль состоит только из букв',
    'upper': 'Отсутствуют заглавные буквы',
    'lower': 'Отсутствуют строчные буквы',
    'spec': 'Отсутствуют спецсимволы в пароле',
    'bad_symbols': 'В пароле использованы непредусмотренные символы'
}

bad_symbols = ['!', '@', '$', '%', '^', '`', '&', '(', ')', '+', '=', '_', '~']
password = 'Aafaf*al'

# Проверяем длину пароля
if len(password) == 8:
    errors_dict.pop('length')

# Проверяем, что пароль НЕ состоит только из цифр
if not password.isdigit():
    errors_dict.pop('digits')

# Проверяем, что пароль НЕ состоит только из букв
if not password.isalpha():
    errors_dict.pop('letters')

# Проверяем, есть ли в пароле заглавные буквы
if password.lower() != password:
    errors_dict.pop('upper')

# Проверяем, есть ли в пароле строчные буквы
if password.upper() != password:
    errors_dict.pop('lower')

# Проверяем, есть ли в пароле специальные символы
if '*' in password or '-' in password or '#' in password:
    errors_dict.pop('spec')
    # Проверяем, встречаются ли спец символы в пароле несколько раз
    if password.count('*') > 1 or password.count('-') > 1 or password.count('#') > 1:
        errors_dict['spec_count'] = 'Какой-то из спецсимволов в пароле использован более одного раза'

# Проверяем, есть ли в пароле запрещенные символы
if len(set(password).intersection(set(bad_symbols))) == 0:
    errors_dict.pop('bad_symbols')

# Проверяем результирующую длину чек-листа
if len(errors_dict) > 0:
    print(list(errors_dict.values()))
else:
    print('Пароль идеален!')
