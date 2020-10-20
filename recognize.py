#Importando as ferramentas
import face_recognition as fr
import cv2
import os.path
import numpy as np
import json
from datetime import date, datetime

#Captura de video
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

#Criando os arrays para as faces
known_face_encodings = []
known_face_names = []

#Ponto de carregar os codigos de faces
caminhos = os.listdir('training_sucsess')

#Percorre o codigo de faces
for nome in caminhos:
    caminho = ('training_sucsess/'+nome)
    arquivos = os.listdir(caminho)
    for arq in arquivos:
        enconding = np.loadtxt('training_sucsess/'+nome+'/'+arq);

        #Adiciona os codigos nos arrays
        known_face_encodings.append(enconding)
        known_face_names.append(nome)

#Cria outros arrays para inicializar o trabalho de reconhecimento
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
dados = []

#Reconhecendo o rosto da pessoa aparecendo na webcam
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame % 2 == 0:
        
        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)
        face_names = []
          
        for face_enconding in face_encodings:
            
            matches = fr.compare_faces(known_face_encodings, face_enconding)
            name = "Nao desaparecido"

            distance = fr.face_distance(known_face_encodings, face_enconding)
            best_match_index = np.argmin(distance)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            face_names.append(name)

    process_this_frame += 1

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 1
        right *= 1
        bottom *= 1
        left *= 1

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        past = 'recognized/'+name
        data_atual = date.today()
        dados.append({
            'Nome': name,
            'Data' : data_atual.strftime('%d/%m/%Y'),
        })

        if os.path.exists(past):
            past2 = past+'/'+name
            cv2.imwrite(past2+'.png', rgb_small_frame)
            with open(past2+'.json', 'w') as json_file:
                json.dump(dados, json_file, indent = 3, ensure_ascii = False)
        else:
            os.mkdir(past)
            past2 = past+'/'+name
            cv2.imwrite(past2+'.png', rgb_small_frame)
            with open(past2+'.json', 'w') as json_file:
                json.dump(dados, json_file, indent = 3, ensure_ascii = False)
            
    cv2.imshow('Video', frame)

    # letra 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()