import cv2

classificate = cv2.CascadeClassifier("frontal_face.xml")
cam = cv2.VideoCapture(0)
sample = 1
numberSample = 25
idPeople = input('Digite seu identificador: ')
width, height = 220, 220
print("Capturando as faces")

while (True):
    connect, img = cam.read()
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    facesDetection = classificate.detectMultiScale(imggray, scaleFactor=1.5, minSize=(100, 100))

    for (x, y, l, a) in facesDetection:
        cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 255), 2)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            imgFace = cv2.resize(imggray[y:y + a, x:x + l], (width, height))
            cv2.imwrite("fotos/pessoa." + str(idPeople) + "." + str(sample) + ".jpg", imgFace)
            print("[foto" + str(sample) + "capturada com sucesso]" )
            sample += 1

    cv2.imshow("Face", img)
    #cv2.waitKey(1)

    if (sample >= numberSample + 1):
        break

print("Faces capturadas com sucesso")
cam.release()
cv2.destroyAllWindows()
