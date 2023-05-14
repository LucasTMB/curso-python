from mongoengine import Document, StringField

class Contato(Document):
    nome = StringField(required=True)
    telefone = StringField(required=True)
