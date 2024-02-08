import re
#Ocorrencia presente uma ou mais vezes
um_ou_mais = re.compile('pytho+n')
mol = um_ou_mais.search('Curso de python')
print(mol.group())
#Ocorrencia presente uma ou mais vezes
mol = um_ou_mais.search('Curso de pythooooon')
print(mol.group())
#Erro caso não encontre uma ou mais ocorrencias
mol = um_ou_mais.search('Curso de Pythn')
print(mol.group())