import re
# Ocorrencia caso o 'o' esteja presente ou ausente
zero_ou_mais = re.compile('pytho*n')
mol = zero_ou_mais.search('Curso de python')
print(mol.group())

# Ocorrencia caso o 'y' esteja presente multiplas vezes, bem como o 'o'
zero_ou_mais = re.compile('py*tho*n')
mol = zero_ou_mais.search('Curso de pyyyyyythoooooon')
print(mol.group())

#Ocorrencia caso o 'o' esteja ausente
mol = zero_ou_mais.search('Curso de pythn')
print(mol.group())

#Ocorrencia caso o 'y' esteja ausente
mol = zero_ou_mais.search('Curso de pthn')
print(mol.group())

# ocorrencia caso 'y' 'h' e o 'o' estejam ausentes
zero_ou_mais = re.compile('py*th*o*n')
mol = zero_ou_mais.search('Curso de ptn')
print(mol.group())

# Erro pois não tera ocorrencia que não exista o n
mol = zero_ou_mais.search('Curso de pt')
print(mol.group())