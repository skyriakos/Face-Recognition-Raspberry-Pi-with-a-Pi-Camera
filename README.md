# Face-Recognition-Raspberry-Pi-with-a-Pi-Camera
A Software for Face Recognition on a Raspberry Pi 4/5 with a Pi Camera

📸 How It Works

Capture training photos of each person using the Pi Camera
Train the model by generating 128-dimensional face encodings
Recognize faces in real-time from the live camera feed


🛠️ Hardware Requirements

Raspberry Pi 4 (2GB RAM or more recommended)
Raspberry Pi Camera Module v2 or v3
Monitor, keyboard, mouse (or SSH access)


⚙️ Software Requirements & Installation
Make sure your Raspberry Pi OS is up to date:
bashsudo apt update && sudo apt upgrade -y
sudo apt install -y cmake libopenblas-dev liblapack-dev
Install the required Python libraries:
bashpip3 install face_recognition opencv-python picamera2 --break-system-packages

⚠️ Note: Installing dlib (required by face_recognition) takes 20–40 minutes on the Raspberry Pi because it compiles from source. This is normal — just let it run.


🚀 Usage
Step 1 — Set up the project folder
bashmkdir /home/pi/gesichtserkennung
mkdir /home/pi/gesichtserkennung/fotos
cd /home/pi/gesichtserkennung
Clone or copy the scripts into this folder.
Step 2 — Capture training photos
Run the photo capture script for each person you want to recognize:
bashpython3 foto_aufnehmen.py
Enter the person's name when prompted. The script will automatically take 20 photos. Repeat this for every person.
After this step your folder should look like:
fotos/
├── Person1/
│   ├── 0.jpg
│   ├── 1.jpg
│   └── ...
└── Person2/
    ├── 0.jpg
    └── ...
Tips for better accuracy:

Use good, even lighting
Look at the camera from slightly different angles
Try with and without glasses if you wear them

Step 3 — Train the model
bashpython3 training.py
This reads all photos, computes face encodings, and saves them to encodings.pickle. You'll see a checkmark for each successfully processed photo.
Step 4 — Start real-time recognition
bashpython3 erkennung.py
A window will open showing the live camera feed. Recognized faces will be labeled with their name in green. Press q to quit.



🔧 Configuration
In erkennung.py you can adjust the tolerance value to tune accuracy:
pythonmatches = face_recognition.compare_faces(daten["encodings"], encoding, tolerance=0.5)
ValueEffect0.4Stricter — less false positives, may miss faces0.5Default — good balance0.6More lenient — works better in low light

📦 Dependencies
LibraryPurposeface_recognitionFace detection and encodingdlibUnderlying ML model (installed automatically)opencv-pythonCamera stream and drawingpicamera2Raspberry Pi camera interfacenumpyNumerical operations

💡 Performance Tips

The frame is scaled to 25% before processing to improve speed (~8–12 FPS on Pi 4)
Add more training photos per person for better accuracy
Make sure the camera is well-lit for best results
