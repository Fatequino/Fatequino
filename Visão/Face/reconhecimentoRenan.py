import os
import glob # será usada para percorrermos arquivos de imagens
import _pickle as cPickle # gravação do arquivo de treinamento
import cv2
import dlib
import numpy as np

# para reconhecer, primeiro temos que detectar as faces
detectorFace = dlib.get_frontal_face_detector()
detectorPontos = dlib.shape_predictor("./recursos/shape_predictor_68_face_landmarks.dat")
reconhecimentoFacial = dlib.face_recognition_model_v1("./recursos/dlib_face_recognition_resnet_model_v1.dat") # passando um arquivo .dat treinado para reconhecimento facial com CNN

indice = {}
idx = 0
descritoresFaciais = None

# laço para percorrer todas as imagens de treinamento
for arquivo in glob.glob(os.path.join("./fotosTreinamento", "*.jpg")): # arquivo vai receber cada uma das imagens. O os vai funcionar pra qualquer SO
    # leitura de cada imagem
    imagem = cv2.imread(arquivo)
    # depois de ler as imagens, vamos detectar as faces
    facesDetectadas = detectorFace(imagem, 1)
    numeroFacesDetectadas = len(facesDetectadas) # quantas faces ele está detectando.
    # Para fazer o treinamento com o dlib, temos que ter apenas 1 face por imagem para não confunfir o algoritmo
    #print(numeroFacesDetectadas)
    if numeroFacesDetectadas > 1:
        print("Há mais de uma face na imagem {}".format(arquivo))
        exit(0)
    elif numeroFacesDetectadas < 1:
        print("Nenhuma face encontrada no arquivo {}".format(arquivo))
        exit(0)
    for face in facesDetectadas: # essa variável armazena os bounding boxes das faces detectadas
        # extraindo os pontos faciais
        pontosFaciais = detectorPontos(imagem, face) # imagem = o todo face = o pedacinho da imagem com bounding box. Passamos só a parte necessária
        # o treinamento é basicamente criar um descritor facial
        descritorFacial = reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais) # esse compute vai computar as características específicas dessa face
        # o resultado será um vetor com 128 posições que vai descrever a face encontrada
        # basicamente, a aprendizagem é a geração desses vetores com as características mais importantes
        #print(format(arquivo))
        #print(len(descritorFacial))
        #print(descritorFacial)

        # conversões e uns arquivos para usarmos nos testes
        listaDescritorFacial = [df for df in descritorFacial] # transformando em uma lista de tamanho 128
        # verificar o que exatamente foi feito
        #print(listaDescritorFacial)
        #agora vamos converter essa lista em um vetor do tipo numpy
        npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
        # ver exatamente o que foi feito
        #print(npArrayDescritorFacial)

        npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, : ] # vamos criar uma nova coluna
        #print(npArrayDescritorFacial)

        # concatenando o npArrayDescritorFacial com o descritoresFaciais
        if descritoresFaciais is None:
            descritoresFaciais = npArrayDescritorFacial
        else:
            descritoresFaciais = np.concatenate((descritoresFaciais, npArrayDescritorFacial), axis = 0)

        indice[idx] = arquivo
        idx += 1
    #cv2.imshow("Treinamento: ", imagem)
    #cv2.waitKey(0)

print("Tamanho: {} Formato: {}".format(len(descritoresFaciais), descritoresFaciais.shape)) # 8 linhas, 128 colunas. Cada linha tem o valor da característica
# para vizualizar
print(descritoresFaciais)
# nome das imagens
print(indice)

# para fechar, vamos gravar os descritores em um arquivo
np.save("./recursos/descritores_renan.npy", descritoresFaciais) # aqui passamos o caminho onde será salvo o arquivo, e o .npy é o formato q o dlib precisa o ler
# também precisamos gravar o indice
with open("./recursos/indices_renan.pickle", 'wb') as f: # .pickle é bem utilizado em machine learning para salvar classificadores
    cPickle.dump(indice, f)

#cv2.destroyAllWindows()