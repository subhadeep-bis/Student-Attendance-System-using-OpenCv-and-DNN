# packages
import cv2
import os
import argparse
from imutils.video import VideoStream
import imutils
import time

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path of the folder where photo will be dumped")
args = vars(ap.parse_args())

# setup the path for the images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initializiong video stream for collection of data
print("[INFO] starting video stream....")
vs = VideoStream(src=0).start()
time.sleep(2.0)

i=1
while(True):
	# grab the frame from the threaded video stream
	frame = vs.read()

	# resize the picture so that every picture is of same size
	frame = imutils.resize(frame, width=600)
	(h, w) = frame.shape[:2]

	imagePath = os.path.join(BASE_DIR, args["dataset"])
	
	name = str(i) + ".png"
	imagePath = os.path.join(imagePath, name)
	print(imagePath)
	cv2.imwrite(imagePath,frame)

	# updating name
	i+=1

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, break the loop
	if key == ord("q"):
		break

imagePath = os.path.join(BASE_DIR, args["dataset"])
print()
print("****************************************************************************************************")
print("Check the ./"+ args["dataset"] +"/ directory to get your pictures")
print("****************************************************************************************************")

cv2.destroyAllWindows()
vs.stop()
