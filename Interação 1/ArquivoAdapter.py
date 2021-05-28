from pymongo import MongoClient
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

class ArquivoAdapter(LogicAdapter):
  def __init__(self, chatbot, **kwargs):
    super().__init__(chatbot, **kwargs)

  def can_process(self, statement):
    subject = ['arquivo', 'arquivos', 'atestado', 'atestados', 'declaracao', 'declaracoes', 'documento', 'documentos', 'estagio', 'calendario']

    if any(x in statement.text.lower().split() for x in subject):
      return True

    return False

  def process(self, statement, _):
    mensagem = 'Tenho aqui alguns arquivos que podem ser uteis pra você. Dê uma olhada nos arquivos da Fatec aqui no meu repositório do <a href="https://drive.google.com/drive/folders/1n0GuGD-meSgFtyFqD6r3AH-7_LG4Q72u?usp=sharing">drive</a>'

    msg = Statement(text=mensagem)
    msg.confidence = 1

    return msg