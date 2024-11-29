from picamera2 import Picamera2
from time import sleep
camera = Picamera2()
# Start the camera preview
camera.start()
sleep(5) # Allow time for adjustments
# Capture the image
camera.capture_file('image.jpg')
print("Image captured!")
# Stop the preview
camera.stop_preview()
