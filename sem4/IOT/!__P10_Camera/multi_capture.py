import time
from picamera2 import Picamera2, Preview

# initialise camera
picam = Picamera2()

# initialise an empty image configuration
config = picam.create_preview_configuration()
picam.configure(config)

picam.start_preview(Preview.QTGL)  # start preview window
picam.start()  # start camera

print("\nPress Enter to Capture image or type 'n' to exit\n")

i = 1
while not input("Capture? [Y/n] "):
    picam.capture_file("image%d.jpg" % i)
    print("Captured image%d.jpg\n" % i)
    i += 1

picam.close()
