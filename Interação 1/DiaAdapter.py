from pymongo import MongoClient
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from datetime import date

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

class DiaAdapter(LogicAdapter):
  def __init__(self, chatbot, **kwargs):
    super().__init__(chatbot, **kwargs)

  def can_process(self, statement):
    dias = ['hoje', 'amanhã', 'amanha', 'segunda', 'terça', 'terca', 'quarta', 'quinta', 'sexta', 'sábado', 'sabado', 'domingo']

    if any(x in statement.text.lower().split() for x in dias):
      return True

    return False

  def process(self, statement, _):
    dia = self.obter_dia(statement.text)
    cliente = MongoClient("mongodb://localhost:27017")
    db = cliente['chatterbot-database']
    aulasInfo = db.aulasInfo
    result = list(aulasInfo.find({'Dia': dia}))

    if len(result) == 0:
      resp = Statement(text='{} não tem aulas, mas aproveite para estudar!'.format(obter_dia_da_semana(dia)))
      resp.confidence = 1
      return resp

    mensagem = '{} é dia de '.format(obter_dia_da_semana(dia))

    for d in result:
      mensagem = '{} {} às {} para o ciclo {} com {} <br>'.format(mensagem, d['Disciplina'], d['Horario'], d['Ciclo'] ,d['Professor'])

    mensagem.replace(',', '.', len(mensagem) -1)

    msg = Statement(text=mensagem)
    msg.confidence = 1

    return msg
    

  def obter_dia(self, mensagem):
    if 'hoje' in mensagem.lower():
      dia = date.today().weekday() + 2
      print(dia)
      return str(dia if dia < 8 else 1)
    
    if 'amanhã' in mensagem.lower() or 'amanha' in mensagem.lower():
      dia = date.today().weekday()
      return str(dia + 2 if dia != 6 else 2)

    if 'segunda' in mensagem.lower():
      return '2'

    if 'terca' in mensagem.lower() or 'terça' in mensagem.lower():
      return '3'

    if 'quarta' in mensagem.lower():
      return '4'

    if 'quinta' in mensagem.lower():
      return '5'

    if 'sexta' in mensagem.lower():
      return '6'

    if 'sábado' in mensagem.lower() or 'sabado' in mensagem.lower():
      return '7'

    if 'domingo' in mensagem.lower():
      return '1'

