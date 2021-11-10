def inserir(lista):#Iserir contatos

    while True:
        email = (input('E-mail: '))
        if not existeContato(lista, email):
            break
        else:
            print('E-mail já utilizado')

    contato = {
        'nome':(input('Nome: ')),
        'telefone':int(input('Telefone: ')),
        'email': email,
        'twitter':(input('Twitter: ')),
        'instagram':(input('Instagram: '))
    }
    lista.append(contato)

    print('\nCADATRO REALIZADO COM ÊXITO!\n')


def editar(lista):#Editar contatos
    print('=======================================\n')
    print('           EDITAR CONTATO\n ')
    if len(lista) > 0:
        email = input('E-mail do contato:')
        if existeContato(lista, email):
            for contato in lista:
                if contato['email'] == email:
                    print('\n==============================================')
                    print('Nome: {}'.format(contato['nome']))
                    print('Telefone: {}'.format(contato['telefone']))
                    print('Email: {}'.format(contato['email']))
                    print('Twitter: {}'.format(contato['twitter']))
                    print('Instagram: {}'.format(contato['instagram']))
                    print('=============================================\n')

                    contato['nome'] = input('Novo nome: ')
                    contato['telefone'] = int(input('Novo telefone: '))
                    contato['email'] = input('Novo e-mail: ')
                    contato['twitter'] = input('Novo twitter: ')
                    contato['instagram'] = input('Novo instagram: ')

                    print('\nCONTATO EDITADO COM ÊXITO!')
                    break

        else:
            print('CONTATO NÃO EXISTE')
    else:
        print('CONTATO NÃO EXISTE')


def excluir(lista):#Excluir contatos
    print('=======================================\n')
    print('           EXCLUIR CONTATO\n')
    if len(lista) > 0:
        email = input('E-mail do contato:')
        if existeContato(lista, email):
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print('\n=================================================')
                    print('Nome: {}'.format(contato['nome']))
                    print('Telefone: {}'.format(contato['telefone']))
                    print('Email: {}'.format(contato['email']))
                    print('Twitter: {}'.format(contato['twitter']))
                    print('Instagram: {}'.format(contato['instagram']))
                    print('=================================================\n')

                    del lista[i]

                    print('\nCONTATO APAGADO COM ÊXITO!\n')
                    break

        else:
            print('CONTATO NÃO EXISTE')
    else:
        print('CONTATO NÃO EXISTE')

def pesquisar(lista):#Pesquisar contatos
    print('=======================================\n')
    print('           PESQUISAR CONTATO\n')
    if len(lista) > 0:
        email = input('E-mail do contato: ')
        if existeContato(lista, email):
            for contato in lista:
                if contato['email'] == email:
                    print('\n=================================================')
                    print('Nome: {}'.format(contato['nome']))
                    print('Telefone: {}'.format(contato['telefone']))
                    print('Email: {}'.format(contato['email']))
                    print('Twitter: {}'.format(contato['twitter']))
                    print('Instagram: {}'.format(contato['instagram']))
                    print('=================================================\n')
                    break
        else:
            print('\nCONTATO NÃO EXISTE\n')
    else:
        print('\nCONTATO NÃO EXISTE\n')

def salvarContatos(lista):#Salvar contatos em um arquivo txt
    arquivo = open('contatos.txt', 'w')

    for contatos in lista:

        arquivo.write('{},{},{},{},{}\n'.format(contatos['nome'], contatos['telefone'], contatos['email'], contatos['twitter'], contatos['instagram']))
    
    arquivo.close()

def carregarContatos(lista):#Carregar os contatos do arquivo txt

    try:
        arquivo = open('contatos.txt', 'r')

        for linha in arquivo.readlines():
            coluna = linha.strip().split('#')

            contato = {
                'nome': [0],
                'telefone': [1],
                'email': [2],
                'twitter': [3],
                'instagram': [4]
            }

            lista.append(contato)

        arquivo.close()

        return lista
    except FileNotFoundError:
        pass

def existeContato(lista, email):#Confirmar a existencia do contato
    if len(lista) > 0:
        for contato in lista:
            if contato['email'] == email:
                return True
    return False


def MENU():#Principal
    lista = []
    carregarContatos(lista) 

    while True:
        print('\n====== AGENDA TELEFÔNICA ======')
        print('''
   1 - Inserir
   2 - Pesquisar
   3 - Editar
   4 - Apagar

   0 - Sair
''')
        opcao = eval(input('> '))

        if opcao == 1:
            inserir(lista)
            salvarContatos(lista)
        elif opcao == 2:
            pesquisar(lista)
        elif opcao == 3:
            editar(lista)
            salvarContatos(lista)
        elif opcao == 4:
            excluir(lista)
            salvarContatos(lista)
        elif opcao == 0:
            print('\nSAINDO...')
            break
        else:
            print('\nOPÇÃO NÃO EXISTE')

MENU()