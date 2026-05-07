import face_recognition
import os
import pickle

bekannte_encodings = []
bekannte_namen = []

print("Starting training...")

for person in os.listdir("fotos"):
    person_path = f"fotos/{person}"
    if not os.path.isdir(person_path):
        continue
    for datei in os.listdir(person_path):
        if not datei.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        bild = face_recognition.load_image_file(f"{person_path}/{datei}")
        encodings = face_recognition.face_encodings(bild)
        if encodings:
            bekannte_encodings.append(encodings[0])
            bekannte_namen.append(person)
            print(f"✓ {person}/{datei}")
        else:
            print(f"✗ No face found in {person}/{datei} - skipping")

with open("encodings.pickle", "wb") as f:
    pickle.dump({"encodings": bekannte_encodings, "namen": bekannte_namen}, f)

print(f"\nTraining complete! {len(bekannte_encodings)} face(s) encoded.")
