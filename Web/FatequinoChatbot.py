class FatequinoChatbot():
    def __init__(self, bot, Trainer):
        self.bot = bot
        self.trainer = Trainer(self.bot)

    def treinarBot(self, conversa):
        return self.trainer.train(conversa)

    def mensagemEnviada(self, mensagemRecebida):
        if ( float(self.bot.get_response(mensagemRecebida).confidence) > 0.5):
            return self.bot.get_response(mensagemRecebida)
        return "Ainda estou timido para responder sobre isso"