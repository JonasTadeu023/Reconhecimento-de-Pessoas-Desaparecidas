import face_recognition as fr
import cv2

video_capture = cv2.VideoCapture(0)

enc = fr.load_image_file("images_missing/Jonas/Jonas.jpg")
enconding = fr.face_encodings(enc)[0]

outra_pessoa = fr.load_image_file("not_missing/João.D.jpg")
outra_pessoa_enc = fr.face_encodings(outra_pessoa)[0]

known_face_encodings = [
    enconding,
    outra_pessoa_enc
]

known_face_names = [
    "Jonas",
    "João"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame      = video_capture.read()
    small_frame     = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
         face_locations = fr.face_locations(rgb_small_frame)
         face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

         face_names = []
         matches = fr.compare_faces(known_face_encodings[0], face_encodings)
         name = "Estranho"

         if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 2
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    # letra 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()