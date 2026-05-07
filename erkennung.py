import face_recognition
import cv2
import pickle
import picamera2
import numpy as np

# Load encodings
print("Loading face encodings...")
with open("encodings.pickle", "rb") as f:
    daten = pickle.load(f)

print(f"Loaded {len(daten['encodings'])} face(s): {set(daten['namen'])}")
print("Starting camera... Press 'q' to quit.")

cam = picamera2.Picamera2()
cam.configure(cam.create_preview_configuration(main={"size": (640, 480)}))
cam.start()

while True:
    frame = cam.capture_array()

    # Scale down for faster processing
    klein = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(klein, cv2.COLOR_BGR2RGB)

    positionen = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, positionen)

    for encoding, (oben, rechts, unten, links) in zip(encodings, positionen):
        matches = face_recognition.compare_faces(daten["encodings"], encoding, tolerance=0.5)
        name = "Unknown"

        if True in matches:
            distanzen = face_recognition.face_distance(daten["encodings"], encoding)
            bester = np.argmin(distanzen)
            if matches[bester]:
                name = daten["namen"][bester]

        # Scale back up
        oben, rechts, unten, links = oben * 4, rechts * 4, unten * 4, links * 4

        cv2.rectangle(frame, (links, oben), (rechts, unten), (0, 255, 0), 2)
        cv2.putText(frame, name, (links, oben - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.stop()
cv2.destroyAllWindows()
