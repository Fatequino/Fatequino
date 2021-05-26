from pymongo import MongoClient
from chatterbot.logic import LogicAdapter
import difflib

class HorariosLocaisAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        subject = ['secretaria', 'biblioteca']
        question = ['abre', 'quando', 'fecha']

        if any(x in statement.text.split() for x in question):
            if any(x in statement.text.split() for x in subject):
                return True

        return False


    def process(self, statement, _):
        from chatterbot.conversation import Statement
        import requests

        cliente = MongoClient("mongodb://localhost:27017")
        db = cliente['chatterbot-database']
        horarioLocal = db.horarioLocal
        result = horarioLocal.find({})
        locais = list(filter(lambda f: f['Local'].lower() in statement.text.lower(), result))

        if len(locais) == 0:
            return Statement(text='')

        mensagem = ''

        for local in locais:
            mensagem += 'A {} abre {} das {} às {} <br>'.format(
                local['Local'], local['Dias'], local['HorarioInicio'], local['HorarioFim']
            )

        response_statement = Statement(text=mensagem)
        response_statement.confidence = 1 

        return response_statement