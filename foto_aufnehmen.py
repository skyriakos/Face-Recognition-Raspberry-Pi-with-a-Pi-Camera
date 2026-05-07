import picamera2
import cv2
import os
import time

name = input("Enter the name of the person: ")
os.makedirs(f"fotos/{name}", exist_ok=True)

cam = picamera2.Picamera2()
cam.start()
time.sleep(1)

print(f"Taking 20 photos of '{name}'...")

for i in range(20):
    frame = cam.capture_array()
    cv2.imwrite(f"fotos/{name}/{i}.jpg", frame)
    time.sleep(0.3)
    print(f"Photo {i+1}/20")

cam.stop()
print("Done! Photos saved.")
