from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sys
sys.path.append('/usr/local/lib/python3.4/site-packages')
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (640, 480))

time.sleep(0.1)

#obtain camera input array
for frame in camera.capture_continuous(rawCapture, format = "bgr", use_video_port = True):
    image_preview = frame.array

    #generate preview window
    cv2.imshow("Frame", image_preview)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    #capture and display preview
    if key == ord("q"):
        cv2.imshow("Capture", image_preview)
        cv2.imwrite("test_image.jpeg", image_preview)
        time.sleep(.1)
        cv2.destroyAllWindows()

    #exit program
    if key == ord("f"):
        cv2.destroyAllWindows()
        break

   
    
