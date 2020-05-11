# -*- coding: utf-8 -*-

# COMO USAR
# python recognize_faces_video.py --encodings encodings.pickle
# python recognize_faces_video.py --encodings encodings.pickle --display 0
# python recognize_faces_video.py --encodings encodings.pickle --detection-method cnn

# importa as bibliotecas necessárias
from imutils.video import VideoStream # lib de stream de video
import face_recognition # lib que faz o reconhecimento facial
import argparse # utilizado para parsear argumentos da linha de comando
import imutils # funcoes matematicas
import pickle # ler/escrever arquivos .pickle
import time
import cv2 # OpenCV

# declara e parseia os argumentos da linha de comando
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="caminho do arquivo .pickle contendo os encodings faciais")
ap.add_argument("-y", "--display", type=int, default=1,
	help="mostra ou não o video em tempo real")
ap.add_argument("-d", "--detection-method", type=str, default="hog",
	help="modelo de deteccao facial a ser utilizado: `hog` ou `cnn`")
args = vars(ap.parse_args())

# carrega o arquivo contendo os dados de encoding facial
print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

# inicializa o stream de video
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
writer = None
time.sleep(2.0)

while True:
	# pega o frame de video
	frame = vs.read()

	# converte o frame de BGR (ordem de canais de cores que o imutils/OpenCV usa) para RGB (utilizado pelo face_recognition)
	# e redimensiona para 750px (melhor perfomance)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	rgb = imutils.resize(frame, width=750)
	r = frame.shape[1] / float(rgb.shape[1])

	# detecta as coordenadas (x, y) das caixas correspondentes aos rostos detectados
	# e computa os encodings faciais
	boxes = face_recognition.face_locations(rgb,
		model=args["detection_method"])
	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []

	# itera sobre os encodings computados
	for encoding in encodings:
		# tenta achar encodings similares dos computados com os presentes no arquivo
		# definido na linha de comando
		# retorna uma lista de booleanos
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Desconhecido"

		# verifica se encontrou algo
		if True in matches:
			# salva os indices de todas as faces encontradas
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# itera sobre os indices encontrados e instancia um dictionary
			# com o numero de vezes que cada face foi encontrada
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# verifica qual face teve o maior numero de reconhecimentos
			name = max(counts, key=counts.get)

		# adiciona na lista de nomes
		names.append(name)

	# itera sobre as faces reconhecidas
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# redimensiona a imagem para o tamanho original
		top = int(top * r)
		right = int(right * r)
		bottom = int(bottom * r)
		left = int(left * r)

		# escreve o nome da face reconhecida no video
		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 255, 0), 2)

	# verifica se é para mostrar o video na tela
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# caso a letra `q` seja pressionada, encerra a execução do programa
		if key == ord("q"):
			break

# dispose é sempre bom
cv2.destroyAllWindows()
vs.stop()