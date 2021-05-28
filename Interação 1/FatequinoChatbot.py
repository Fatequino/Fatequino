from pymongo import MongoClient
from flask import send_file
import json

# classe que trata as mensagens
class FatequinoChatbot():
    def __init__(self, bot, Trainer):
        self.bot = bot
        self.trainer = Trainer(self.bot)
        # carrega conversas que o bot ja entende
        self.conversas = json.loads(open('conversas.json', 'r').read())
        self.conversasDesconhecidas = []

    def treinarBot(self, conversa):
        return self.trainer.train(conversa)

    def mensagemEnviada(self, mensagemRecebida):
        print(mensagemRecebida)
        # verifica se o bot consegue responder a mensagem
        if ( float(self.bot.get_response(mensagemRecebida).confidence) > 0.5):
            print('show')
            return self.bot.get_response(mensagemRecebida)
        # verifica se o bot sabe responder com as conversas registradas no arquivo conversas.json    
        if mensagemRecebida in self.conversas:
            print('show')
            return self.bot.get_response(mensagemRecebida)
        else:
            # grava as conversas que o bot nao sabe responder em um arquivo
            if not (mensagemRecebida in self.conversas):
                self.conversasDesconhecidas.append(mensagemRecebida)
                with open('conversasSemResposta.json', 'w', encoding='utf-8') as gravarConversa:
                    json.dump(self.conversasDesconhecidas, gravarConversa, ensure_ascii=False, indent=4, separators=(',', ':'))
                return "Ainda não sei te responder sobre isso, mas irei pesquisar para conseguir te responder."

    # carrega dados inseridos pelo postman no banco de dados mongoDB
    def setHorarios(self, data):
        cliente = MongoClient("mongodb://localhost:27017")
        db = cliente['chatterbot-database']
        aulasInfo = db.aulasInfo
        aulasInfo.drop()
        aulasInfo.insert(data)
        return "Horários inseridos com sucesso"
    
    def setHorariosLocais(self, data):
        cliente = MongoClient("mongodb://localhost:27017")
        db = cliente['chatterbot-database']
        horarioLocal = db.horarioLocal
        horarioLocal.drop()
        horarioLocal.insert(data)
        return "Horários dos locais inseridos com sucesso"