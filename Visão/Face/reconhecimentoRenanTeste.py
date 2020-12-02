import os
import glob
import _pickle as cPickle
import dlib
import cv2
import numpy as np

detectorFace = dlib.get_frontal_face_detector()
detectorPontos = dlib.shape_predictor("./recursos/shape_predictor_68_face_landmarks.dat")
reconhecimentoFacial = dlib.face_recognition_model_v1("./recursos/dlib_face_recognition_resnet_model_v1.dat")
indices = np.load("./recursos/indices_renan.pickle", allow_pickle=True) # arquivo que geramos no treinamento
descritoresFaciais = np.load("./recursos/descritores_renan.npy") # arquivo que geramos no treinamento
limiar = 0.5 # recomendado pela documentação do dlib. Se for limiar = 0 significaria que a imagem teria q ser igualzinha, fazendo reconhecer menos faces.
            # se dá valores maiores, provavelmente não estão na base de dados. Se o limkar for muito alto pode ser que outros rostos sejam classificados como ronald tbm

for arquivo in glob.glob(os.path.join("./fotos", "*.jpg")):
    imagem = cv2.imread(arquivo)
    facesDetectadas = detectorFace(imagem, 2)
    for face in facesDetectadas:
        e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
        pontosFaciais = detectorPontos(imagem, face)
        descritorFacial = reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais)
        listaDescritorFacial = [fd for fd in descritorFacial]
        npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
        # adicionando a nova coluna
        npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]

        # aplicando o KNN
        distancias = np.linalg.norm(npArrayDescritorFacial - descritoresFaciais, axis=1) # cálculo da Distancia Euclidiana
        #print("Distâncias: {}".format(distancias))
        minimo = np.argmin(distancias)
        print(minimo)
        distanciaMinima = distancias[minimo] # aqui teremos o valor da distância
        print(distanciaMinima)

        if distanciaMinima <= limiar:
            nome = os.path.split(indices[minimo])[1].split(".")[0]
        else:
            nome = ''

        cv2.rectangle(imagem, (e, t), (d, b), (0, 255, 255), 2)
        #texto = "{} {:.4f}".format(nome, distanciaMinima)
        texto = "Renan".format(nome, distanciaMinima) # não é certeza se é aqui mesmo que colocamos o nome
        cv2.putText(imagem, texto, (d, t), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))

    cv2.imshow("Detector HOG: ", imagem)
    cv2.waitKey(0)
cv2.destroyAllWindows()