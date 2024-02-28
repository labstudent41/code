import time
from picamera2 import Picamera2, Preview

# initialise camera
picam = Picamera2()

# initialise an empty image configuration
config = picam.create_preview_configuration()
picam.configure(config)

picam.start_preview(Preview.QTGL)  # start preview window
picam.start()  # start camera

time.sleep(5)  # wait for 5 seconds
picam.capture_file("image.jpg")  # save image to 'image.jpg'
picam.close()  # close camera
