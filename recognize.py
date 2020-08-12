import face_recognition as fr;
import cv2;
import os.path;
import numpy as np;

video = cv2.VideoCapture(0);

caminhos = os.listdir('training_sucsess');

for nome in caminhos:
    caminho = ('training_sucsess/'+nome);
    arquivos = os.listdir(caminho);
    for arq in arquivos:
        enconding = np.loadtxt('training_sucsess/'+nome+'/'+arq);

        stranger = fr.load_image_file("not_missing/João.D.jpg");
        stranger_econding = fr.face_encodings(stranger)[0];
       
        conhecer_codigos_de_faces = [
            enconding,
            stranger_econding
        ];

        nomes_faces = [
            nome,
            "Desconhecido"
        ];

        face_locations = [];
        face_encodings = [];
        face_names = [];
        process_this_frame = [];

        while True:
            ret, frame = video.read();
            small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25);
            rgb_small_frame = small_frame[:, :, :: -1];

            if process_this_frame:
                face_locations = fr.face_locations(rgb_small_frame);
                face_encodings = fr.face_encodings(rgb_small_frame, face_locations);

                matches = fr.compare_faces(conhecer_codigos_de_faces, face_encodings);
                name = "Estranho";

                if True in matches:
                    first_match_index = matches.index(True);
                    name = nomes_faces[first_match_index];

                    face_names.append(name);
                
            process_this_frame = not process_this_frame;

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4;
                right *= 4;
                bottom *= 4;
                left *= 4;

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2);

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED);
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1);
            
            cv2.imshow('Video', frame);

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break;

        video.release();
        cv2.destroyAllWindows();