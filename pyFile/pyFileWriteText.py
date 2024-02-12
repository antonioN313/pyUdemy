lines = ['Readme', 'Concluindo a seção 11 sobre trabalho com arquivos com Python 3']
with open('../pyUdemy/pyfileConclusion.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
lines = ['Texto em relação ao desenvolvimento de automação de processos',
         'Automação de Processos com Python: Um Guia Completo',
         'O que é a automação de processos com Python?',
         'É a técnica de usar a linguagem de programação Python para automatizar tarefas repetitivas e ',
         'complexas em diversas áreas. Essa ferramenta poderosa permite que você:',
         'automatiza tarefas como coletar dados, enviar emails, formatar documentos e muito mais.',
         'Conecte diferentes sistemas e aplicativos sem esforço, otimizando o fluxo de informações e ',
         'eliminando a necessidade de transferências manuais de dados.']
with open('../pyUdemy/pyfileAutomateProcess.txt', 'w') as f:
    # f.writelines(lines) sera escrito em uma única linha, enquanto a linha 16 separa as linhas com '\n'
    f.write('\n'.join(lines))

with open('../pyUdemy/pyfileConclusion.txt', 'a') as f:
    f.write('\n Por agora, o curso falou principalmente na manipulação de arquivos e diretórios'
            '\n apresentando o método Path, bem como a forma da identificação das \\ em Windows ou //'
            'presente em distribuições Linux baseadas em UNIX, como o MacOS')
