import cv2, os

name = input("Enter your name: ")
path = f"face_data/{name}"
os.makedirs(path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

while count < 30:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face_img = frame[y:y+h, x:x+w]
        cv2.imwrite(f"{path}/{count}.jpg", face_img)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow('Register Face', frame)
    if cv2.waitKey(1) == 27: break

cap.release()
cv2.destroyAllWindows()