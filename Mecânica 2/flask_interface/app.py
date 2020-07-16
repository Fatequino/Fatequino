import random
import trigonometry
from flask import Flask, jsonify, request

app = Flask(__name__)

anguloServoSuperior = ''
anguloServoInferior = ''

# Simulacao dos angulos iniciais dos servos
anguloInferior = 90
anguloSuperior = 90

# TODO: Lista
# 1 - Integrar as chamadas com o arduino, utilizando oa biblioteca RPi.GPIO, essa biblioteca permite uma comunicação via porta serial.
# 2 - Com a integração com o arduino, criar metodo que captura os angulos dos servos motores para serem utilizanos no metodo canMove.
# 3 - Integrar a movimentação do braço, será necessário realizar um estudo sobre como movimentar o braço para cada lado.
# 4 - melhora no algoritmo canMove, o mesmo deverá considerar as movimentações laterais, atualmente não foi possivel considerar 
# a movimentação lateral, pois não foi possivel analisar como a movimentção para as laterais será feita, limitações de angulacao e outras.
# hoje temos apenas a movimentação no eixo Y em que estiver.

@app.route('/moveArm', methods=['POST'])
def moveArm():
    # Aqui será passada a direção que deve ser movido
    data = request.get_json()

    direcao = data['Direcao']
    distancia = data['Distancia']

    global anguloSuperior
    global anguloInferior

    # TODO: Analisar como calcular o angulo de movimento de cada servo motor para 
    # Para efeito de testes iremos assumir que a cada movimentação o angulo dos servos irá mudar em 5 graus
    # tanto para mais quanto para menos
    # variando entre o servo inferior e superior
    positivo = True
    anguloServoSuperior = anguloInferior
    anguloServoInferior = anguloSuperior

    # Decide se haverá aumento nos graus de um servo ou diminuicao:
    if random.randint(0, 100) > 30:
        positivo = True
    else:
        positivo = False
    
    # Decide se esse movimento ocorrerá no servo superior ou inferior
    if random.randint(0, 100) > 30:
        if positivo == True:
            anguloServoSuperior = anguloServoSuperior + distancia
        else:
            anguloServoSuperior = anguloServoSuperior - distancia
    else:
        if positivo == True:
            anguloServoInferior = anguloServoInferior + distancia
        else:
            anguloServoInferior = anguloServoInferior - distancia

    canMove = trigonometry.canMove(anguloServoSuperior, anguloServoInferior)

    if canMove['canMove'] == True:
        anguloSuperior = anguloServoSuperior
        anguloInferior = anguloServoInferior

    Retorno = { 'Sucesso': canMove['canMove'], 'Dados': canMove, 'direcao': direcao, 'anguloServoSuperior': anguloSuperior, 'anguloServoInferior': anguloInferior}

    return jsonify(Retorno), 200

if __name__ == '__main__':
    app.run(debug=True)