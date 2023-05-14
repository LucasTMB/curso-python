from app import cadastrar_contato, listar_contatos, buscar_contato, atualizar_contato, deletar_contato

while True:
    print('O que deseja fazer?')
    print('1 - Cadastrar um contato')
    print('2 - Listar todos os contatos')
    print('3 - Buscar um contato')
    print('4 - Atualizar um contato')
    print('5 - Deletar um contato')
    print('0 - Sair')

    opcao = input('Opção: ')

    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        id = cadastrar_contato(nome, telefone)
        print(f'Contato cadastrado com o ID {id}')

    elif opcao == '2':
        contatos = listar_contatos()
        print('Lista de contatos:')
        for contato in contatos:
            print(f'Nome: {contato.nome}, Telefone: {contato.telefone}')

    elif opcao == '3':
        nome = input('Digite o nome do contato que deseja buscar: ')
        contatos = buscar_contato(nome)
        print('Contatos encontrados:')
        for contato in contatos:
            print(f'Nome: {contato.nome}, Telefone: {contato.telefone}')

    elif opcao == '4':
        nome = input('Digite o nome do contato que deseja atualizar: ')
        novo_nome = input('Digite o novo nome do contato (deixe em branco para manter o atual): ')
        novo_telefone = input('Digite o novo telefone do contato (deixe em branco para manter o atual): ')
        atualizou = atualizar_contato(nome, novo_nome, novo_telefone)
        if atualizou:
            print('Contato atualizado com sucesso')
        else:
            print('Contato não encontrado')

    elif opcao == '5':
        nome = input('Digite o nome do contato que deseja deletar: ')
        deletou = deletar_contato(nome)
        if deletou:
            print('Contato deletado com sucesso')
        else:
            print('Contato não encontrado')

    elif opcao == '0':
        break

    else:
        print('Opção inválida. Tente novamente')
