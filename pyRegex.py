# Phone Number verify without regex
def is_phone_number(text):
    if len(text) != 15:
        return False
    if text[0] != '(':
        return False
    for i in range(1,3):
        if not text[i].isdecimal():
            return False
    if text[4] != ' ':
        return False
    for i in range(5,10):
        if not text[i].isdecimal():
            return False
    if text[10] != '-':
        return False
    for i in range(11,15):
        if not text[i].isdecimal():
            return False
    return True

regex_phone = input("Digite um numero de telefone ")

if not is_phone_number(regex_phone) == True:
    print("Numero de telefone invalido \n")
else:
    print("Numero valido \n")