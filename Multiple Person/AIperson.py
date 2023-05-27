import cv2
import pyttsx3

def count_faces_in_video():

    face_cascade = cv2.CascadeClassifier('C:/Users/lenovo/PycharmProjects/Persons/Harrcascade/haarcascade_frontalface_default.xml')


    cap = cv2.VideoCapture(0)


    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    face_count = 0

    while True:

        ret, frame = cap.read()


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5,minSize=(10,10))


        face_count = len(faces)
        print('face-count=',face_count)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)


        cv2.imshow('Face Detection', frame)


        if face_count > 1:
            engine.say("Only one persons is allowed please go out")
            engine.runAndWait()


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

    print("Face count:", face_count)


count_faces_in_video()
