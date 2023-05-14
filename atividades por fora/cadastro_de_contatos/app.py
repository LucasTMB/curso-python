from mongoengine import connect
from models import Contato

# Conecta ao banco de dados
connect('contatos', host='localhost', port=27017)

def cadastrar_contato(nome, telefone):
    # Cria um novo contato
    contato = Contato(nome=nome, telefone=telefone)

    # Salva o contato no banco de dados
    contato.save()

    return contato.id

def listar_contatos():
    # Lista todos os contatos cadastrados
    return Contato.objects()

def buscar_contato(nome):
    # Busca um contato pelo nome
    return Contato.objects(nome__icontains=nome)

def atualizar_contato(nome, novo_nome=None, novo_telefone=None):
    contato = Contato.objects(nome=nome).first()
    if contato:
        if novo_nome:
            contato.nome = novo_nome
        if novo_telefone:
            contato.telefone = novo_telefone
        contato.save()
        return True
    else:
        return False

def deletar_contato(nome):
    contato = Contato.objects(nome=nome).first()
    if contato:
        contato.delete()
        return True
    else:
        return False