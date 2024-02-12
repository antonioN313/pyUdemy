import random

capitals = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas',
    'Distrito Federal': 'Brasília'
}


for num_tests in range(30):
    file_exam = open(f'test-brazilian-geography-{num_tests + 1}.txt', 'w', encoding='utf-8')
    file_answers = open(f'test-brazilian-geography-answers-{num_tests + 1}.txt', 'w')
    file_exam.write('First Name:\n\nDate:\n\nGrade:\n\n')
    file_exam.write((' ' * 20) + f'Test Brazilian Capital States (Question Test {num_tests + 1}')
    file_exam.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for question_number in range(26):
        correct_aws = capitals[states[question_number]]
        wrong_aws = list(capitals.values())
        del wrong_aws[wrong_aws.index(correct_aws)]
        wrong_aws = random.sample(wrong_aws, 3)
        aws = wrong_aws + [correct_aws]
        random.shuffle(aws)

        file_exam.write(f'{num_tests + 1}. Qual é a capital de {states[question_number]}?\n')
        for i in range(4):
            file_exam.write(f"    {'ABCD'[i]}. {aws[i]}\n")
        file_exam.write("\n")
        file_exam.write(f"{num_tests + 1}. {'ABCD'[aws.index(correct_aws)]}\n")
    file_exam.close()
    file_answers.close()
