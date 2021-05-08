# Code adapted from Solano, Gabriela(2020).
# Reconocimiento Facial | Python – OpenCV.
# Retrieved from: https://github.com/GabySol/OmesTutorials2020
# Adapted by: Group Fatequino

import cv2
import os
import imutils

personName = input('Informe o nome e o RA: ')
dataPath = '/home/naldo/anaconda3/envs/visao/codigos/reconhecimento/Data' #Caminho das imagens armazenadas
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
	print('Pasta criada: ',personPath)
	os.makedirs(personPath)

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('Ronaldo.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:

	ret, frame = cap.read()
	if ret == False: break
	frame =  imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		rosto = auxFrame[y:y+h,x:x+w]
		rosto = cv2.resize(rosto,(150,150),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(personPath + '/rosto_{}.jpg'.format(count),rosto)
		count = count + 1
	cv2.imshow('frame',frame)

	k =  cv2.waitKey(1)
	if k == 27 or count == 300:
		break

cap.release()
cv2.destroyAllWindows()