import cv2

#apre flusso di comunicazione con il dataset
face_cascade = cv2.CascadeClassifier(r"C:\Users\filip\Documents\python\AI\tests\haarcascade_frontalface_default.xml")

#apre videocamera
cap = cv2.VideoCapture(0)

while True:
    #prende i dati dalla camera
    _, img = cap.read()

    #conversione nella scala di grigi
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #prende i frame
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

    #rettangolo
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #aggiorna finestra
    cv2.imshow('Live Facial Recognition', img)

    #esci con la q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#chiudi tutto
cap.release()
