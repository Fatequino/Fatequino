from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from FatequinoChatbot import FatequinoChatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bot = ChatBot('Fatequino Chat Bot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[ 
        'chatterbot.logic.BestMatch',
        {'import_path': 'disciplinaAdapter.DisciplinaAdapter'}  
    ],
    filters=[ 'chatterbot.filters.RepetitiveResponseFilter' ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)

fatequinoChatbot = FatequinoChatbot(bot, ChatterBotCorpusTrainer)
fatequinoChatbot.treinarBot("chatterbot.corpus.portuguese")


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/get", methods=['GET'])
def get_bot_response():
    userText = request.args.get('msg')
    return str(fatequinoChatbot.mensagemEnviada(userText))

@app.route("/aulasInfo", methods=['POST'])
def post_aulas_info():
    data = request.get_json().get('data')
    fatequinoChatbot.setHorarios(data)
    return jsonify({"status":"sucesso"})

if __name__ == "__main__":
    app.run()
