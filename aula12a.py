nome = str(input('Qual é o seu nome? '))
if nome == 'Wellington':
    print('Que nome bonito!')
elif nome == 'Lucas' or nome == 'Ana' or nome == 'Victor':
    print('Seu nome é bem comum no Brazil!')
elif nome in 'Barbara Eduarda Claudia Gabriela Jaqueline':
    print('Um belo nome feminino!')
print('Tenha um bom dia, \033[33;m{}\033[m!'.format(nome))
