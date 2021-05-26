from pymongo import MongoClient
from flask import send_file
import json

class FatequinoChatbot():
    def __init__(self, bot, Trainer):
        self.bot = bot
        self.trainer = Trainer(self.bot)
        self.conversas = json.loads(open('conversas.json', 'r').read())
        self.conversasDesconhecidas = []


    def treinarBot(self, conversa):
        return self.trainer.train(conversa)

    def mensagemEnviada(self, mensagemRecebida):
        print(mensagemRecebida)
        if ( float(self.bot.get_response(mensagemRecebida).confidence) > 0.5):
            print('show')
            return self.bot.get_response(mensagemRecebida)
        if mensagemRecebida in self.conversas:
            print('show')
            return self.bot.get_response(mensagemRecebida)
        else:
            if not (mensagemRecebida in self.conversas):
                self.conversasDesconhecidas.append(mensagemRecebida)
                with open('conversasSemResposta.json', 'w', encoding='utf-8') as gravarConversa:
                    json.dump(self.conversasDesconhecidas, gravarConversa, ensure_ascii=False, indent=4, separators=(',', ':'))
                return "Ainda não sei te responder sobre isso, mas irei pesquisar para conseguir te responder."

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