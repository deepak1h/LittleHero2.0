
import cv2
import audio
import sys


import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message

serial = spi(0, device= 0, gpio=noop())
device = max7219(serial, cascaded= 1, block_orientation=0,rotate= 0, blocks_arranged_in_reverse_order=0)

print("Created device")


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

capWebcam = cv2.VideoCapture(0)

print ("default resolution = " + str(capWebcam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)) + "x" + str(capWebcam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

capWebcam.set(3, 320.0)              # change resolution to 320x240 for faster processing
capWebcam.set(4, 240.0)

                                                        # show updated resolution
print ("updated resolution = " + str(capWebcam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)) + "x" + str(capWebcam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))


while True:

    retval, frame = capWebcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    )
    f=len(faces)
    
    if f>0:
        if i==1:
            with canvas(device) as draw:
                text(draw,(3,0), chr(41), fill="white")
                text(draw,(-1,0), chr(46), fill="white")
                text(draw,(-1,-5), chr(46), fill="white")
            
            #print(faces,i)
            audio.play()
        i+=1
        


        
    else:
        i=0
        with canvas(device) as draw:
            text(draw,(3,0), chr(40), fill="white")
            text(draw,(-1,0), chr(46), fill="white")
            text(draw,(-1,-5), chr(46), fill="white")
            #print(faces,i)
                

#    for (x, y, w, h) in faces:
#        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 200), 2)

#    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       sys.exit() 
