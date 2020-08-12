import face_recognition

djames     = face_recognition.load_image_file("images_missing/Jonas/Jonas.jpg")
djames_enc = face_recognition.face_encodings(djames)[0]

print(djames_enc)