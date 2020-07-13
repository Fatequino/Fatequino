#Code adapted from van Gent, P. (2016).
# Emotion Recognition Using Facial Landmarks, Python, DLib and OpenCV. A tech blog about fun things with Python and embedded electronics.
# Retrieved from: http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/
# Adapted by: Group Fatequino

#Importando os módulos necessários
import cv2
import dlib
#Configurando os objetos necessários
video_capture = cv2.VideoCapture(0) #Objeto da Webcam
detector = dlib.get_frontal_face_detector() #Detector de face
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Identificador de pontos de referência. Nomeie da forma que desejar o arquivo .dat baixado
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)
    detections = detector(clahe_image, 1) #Detecta as faces na imagem
    for k,d in enumerate(detections): #Para cada face detectada
        shape = predictor(clahe_image, d) #Obtém as coordenadas
        for i in range(1,68): #Há 68 pontos de referência em cada face
            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0,0,255), thickness=2) #Para cada ponto, desenhe um círculo vermelho de espessura 2 no frame original 
    cv2.imshow("image", frame) #Exibe o frame
    if cv2.waitKey(1) & 0xFF == ord('q'): #Finalizar a execução ao clicar em 'q'
        break