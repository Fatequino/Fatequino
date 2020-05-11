# -*- coding: utf-8 -*-
# COMO USAR
# python encode_faces.py --dataset dataset --encodings encodings.pickle


# importa as bibliotecas necessárias
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

# declara e parseia os argumentos da linha de comando
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="caminho com as imagens das faces")
ap.add_argument("-e", "--encodings", required=True,
	help="caminho para salvar o arquivo .pickle com os encodings faciais")
ap.add_argument("-d", "--detection-method", type=str, default="hog",
	help="modelo de deteccao facial a ser utilizado: `hog` ou `cnn`")
args = vars(ap.parse_args())

# pega o caminho das imagens
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args["dataset"]))

knownEncodings = []
knownNames = []

# itera sobre as imagens
for (i, imagePath) in enumerate(imagePaths):
	# extrai o nome da pessoa a partir do caminho da imagem
	# Ex: jon_snow.jpg -> jon_snow
	# Isso seguindo o padrão estabelecido nesse algoritmo
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]

	# converte o frame de BGR (ordem de canais de cores que o imutils/OpenCV usa) para RGB (utilizado pelo face_recognition)
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# detecta as coordenadas (x, y) das caixas correspondentes aos rostos detectados
	boxes = face_recognition.face_locations(rgb,
		model=args["detection_method"])

	# e computa os encodings faciais
	encodings = face_recognition.face_encodings(rgb, boxes)

	# itera sobre os encodings computados
	for encoding in encodings:
		# adicionada cada encodings + nome para nossa lista de nomes + encodings
		knownEncodings.append(encoding)
		knownNames.append(name)

# salva os encodings + name no arquivo especificado na linha de comando
print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open(args["encodings"], "wb")
f.write(pickle.dumps(data))
f.close()