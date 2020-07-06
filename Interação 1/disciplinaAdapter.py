from pymongo import MongoClient
from chatterbot.logic import LogicAdapter
import difflib


def obter_dia_da_semana(dia):
    if dia == '1':
        return 'Domingo'
    if dia == '2':
        return 'Segunda'
    if dia == '3':
        return 'Terça'
    if dia == '4':
        return 'Quarta'
    if dia == '5':
        return 'Quinta'
    if dia == '6':
        return 'Sexta'
    if dia == '7':
        return 'Sábado'

class DisciplinaAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        subject = ['disciplina', 'matéria', 'aula']
        question = ['qual', 'quando', 'onde', 'quem']

        if any(x in statement.text.split() for x in question):
            if any(x in statement.text.split() for x in subject):
                return True

        return False


    def process(self, statement, _):
        from chatterbot.conversation import Statement
        import requests

        cliente = MongoClient("mongodb://localhost:27017")
        db = cliente['chatterbot-database']
        aulasInfo = db.aulasInfo
        result = aulasInfo.find({})
        disciplinas = list(filter(lambda f: f['Disciplina'].lower() in statement.text.lower(), result))

        if len(disciplinas) == 0:
            return Statement(text='')

        disciplina = sorted(disciplinas, key=sort_item, reverse=True)[0]

        dia = obter_dia_da_semana(disciplina['Dia'])

        mensagem = 'A disciplina {} ocorreu toda(o) {} às {} com o(a) professor(a) {} na sala {}. São {} aulas.'.format(
            disciplina['Disciplina'], dia, disciplina['Horario'], disciplina['Professor'], disciplina['Sala'], disciplina['Aulas']
        )

        response_statement = Statement(text=mensagem)
        response_statement.confidence = 1 

        return response_statement

def sort_item(item):
    return item['Disciplina']
      