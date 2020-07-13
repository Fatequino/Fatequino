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

class ProfessorAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        subject = ['professor', 'professsora', 'prof']
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
        professores = list(filter(lambda f: f['Professor'].lower() in statement.text.lower(), result))

        if len(professores) == 0:
            return Statement(text='')
        
        
        mensagem = 'O professor(a) {} leciona:\n'.format()

        for professor in professores:
            dia = obter_dia_da_semana(professor['Dia'])

            mensagem += '{} na {} às {} na sala {}\n'.format(
                professor['Disciplina'], dia, professor['Horario'], professor['Sala']
            )

        response_statement = Statement(text=mensagem)
        response_statement.confidence = 1 

        return response_statement
