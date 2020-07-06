import cv2
import os
import numpy as np 

eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagesId () :
    caminho = [os.path.join('fotos_de_treino', f) for f in os.listdir('fotos_de_treino')]
    
    faces = []
    ids = []
    for caminhoImagem in caminho :
        imageFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        Id = int (os.path.split(caminhoImagem) [-1].split('.') [1])
        #print(Id)
        ids.append(Id)
        faces.append(imageFace)

        #cv2.imshow("Face", imageFace)
        #cv2.waitKey(1000)

    return np.array(ids), faces

ids, faces = getImagesId()
print("TREINANDO...")

lbph.train(faces, ids)
lbph.write('classificadorLbph.yml')

print("TREINAMENTO REALIZADO COM SUCESSO...")

