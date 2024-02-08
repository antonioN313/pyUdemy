import re
phone_num = re.compile('(\(\d{2}\) )?(\d{5}-\d{4})')
mol = phone_num.search("Numero telefonico é (87) 99756-1234. Ligue as 19hrs.")
print(mol.group())
mol = phone_num.search("Numero telefonico é 99756-1234. Ligue as 19hrs.")
print(mol.group())