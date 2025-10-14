from keras_facenet import FaceNet
import cv2, os, pickle
import numpy as np

embedder = FaceNet()
face_embeddings = {}
face_dir = "face_data"

for person in os.listdir(face_dir):
    person_path = os.path.join(face_dir, person)
    embeddings = []
    for image in os.listdir(person_path):
        img = cv2.imread(os.path.join(person_path, image))
        face = embedder.extract(img, threshold=0.95)
        if face:
            embeddings.append(face[0]["embedding"])
    if embeddings:
        face_embeddings[person] = np.mean(embeddings, axis=0)

with open("embeddings.pickle", "wb") as f:
    pickle.dump(face_embeddings, f)