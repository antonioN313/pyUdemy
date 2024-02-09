import re
phone_num = re.compile('(\(\d{2}\)) (\d{5}-\d{4})')
Result = phone_num.search("Numero telefonico é (87) 99756-1234. Ligue as 19hrs.")
print('DDD: ' + Result.group(1))
print('Telefone: '+ Result.group(2))
print('DDD e Telefone: ' + Result.group(0))