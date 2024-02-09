import re
phone_num = re.compile(r'\(\d{2}\) \d{5}-\d{4}')
result = phone_num.search('Numero (21) 99873-4555')
print('telefone: ' + result.group())

