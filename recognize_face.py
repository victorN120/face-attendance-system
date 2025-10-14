import cv2, pickle
from keras_facenet import FaceNet
from utils import init_db, mark_attendance
import numpy as np

init_db()
embedder = FaceNet()
with open("embeddings.pickle", "rb") as f:
    known_embeddings = pickle.load(f)

def match_face(embedding):
    min_dist = float("inf")
    identity = None
    for name, db_emb in known_embeddings.items():
        dist = np.linalg.norm(embedding - db_emb)
        if dist < 0.8 and dist < min_dist:
            min_dist = dist
            identity = name
    return identity

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = embedder.extract(frame, threshold=0.95)
    for face in faces:
        x1, y1, x2, y2 = face["box"]
        embedding = face["embedding"]
        name = match_face(embedding)
        if name:
            mark_attendance(name)
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0), 2)

    cv2.imshow("Live Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()