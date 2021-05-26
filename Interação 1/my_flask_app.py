from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from FatequinoChatbot import FatequinoChatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

data = json.loads(open('conversas.json', 'r', encoding='utf-8').read())
trainn = []

for row in data:
    trainn.append(row['question'])
    trainn.append(row['answer'])

#Carrega adaptadores lógicos para treinamento do bot
bot = ChatBot('Fatequino Chat Bot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[ 
        'chatterbot.logic.BestMatch',
        {'import_path': 'disciplinaAdapter.DisciplinaAdapter'},
        {'import_path': 'DiaAdapter.DiaAdapter'}  ,
        {'import_path': 'professorAdapter.ProfessorAdapter'}  ,
        {'import_path': "HorariosLocaisAdapter.HorariosLocaisAdapter"},
        {'import_path': "ArquivoAdapter.ArquivoAdapter"}
    ],
    filters=[ 'chatterbot.filters.RepetitiveResponseFilter' ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)

#Instancia bot para treinar
fatequinoChatbot = FatequinoChatbot(bot, ChatterBotCorpusTrainer)
trainer = ListTrainer(bot)
fatequinoChatbot.treinarBot("chatterbot.corpus.portuguese")
trainer.train(trainn)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/get", methods=['GET'])
def get_bot_response():
    userText = request.args.get('msg')
    userText = remove_pontuacao(userText)
    userText = remove_acentos(userText)
    return str(fatequinoChatbot.mensagemEnviada(userText))

@app.route("/aulasInfo", methods=['POST'])
def post_aulas_info():
    data = request.get_json()
    fatequinoChatbot.setHorarios(data)
    return jsonify({"status":"sucesso"})

@app.route("/horarioLocal", methods=['POST'])
def post_locais_info():
    data = request.get_json()
    fatequinoChatbot.setHorariosLocais(data)
    return jsonify({"status":"sucesso"})

if __name__ == "__main__":
    app.run()

def remove_pontuacao(texto):
    texto_sem_pontuacao = texto
    remover = "!@#$%¨&*()_-+={[}]:;?/\|"
    for x in remover:
        texto_sem_pontuacao = texto_sem_pontuacao.replace(x, '')
    return texto_sem_pontuacao

def remove_acentos(texto):
    texto_sem_acento = texto
    remover_a = "áãàâ"
    remover_e = "èéê"
    remover_i = "íìî"
    remover_o = "òóôõ"
    remover_u = "úùû"
    remover_c = "ç"
    
    for x in remover_a:
        texto_sem_acento = texto_sem_acento.replace(x, 'a')
    
    for x in remover_e:
        texto_sem_acento = texto_sem_acento.replace(x, 'e')

    for x in remover_i:
        texto_sem_acento = texto_sem_acento.replace(x, 'i')

    for x in remover_o:
        texto_sem_acento = texto_sem_acento.replace(x, 'o')

    for x in remover_u:
        texto_sem_acento = texto_sem_acento.replace(x, 'u')

    for x in remover_c:
        texto_sem_acento = texto_sem_acento.replace(x, 'c')

    return texto_sem_acento
 