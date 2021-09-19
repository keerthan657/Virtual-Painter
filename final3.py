# we firstly choose an object of some color and
# get a range of color values to track

import cv2
import numpy as np
import keyboard

# lower and upper colour values for object to track
lowerThresh = np.array([ 48,   0, 232])
upperThresh = np.array([179,  83, 255])

# we need to capture the video
cap = cv2.VideoCapture(0)

# these are the points to be drawn
stack = [[]]
# color to be drawn
color_var = (0,255,0)
# area threshold for object detection
areaThreshold = 0

# this is to make sure that we are
# not repeatedly adding empty stack elements
repeatCondition = True

while(True):

	# this returns frame by frame of our video
	ret, frame = cap.read()
	# this canvas for background
	canvas = np.zeros_like(frame)

	# convert to hsv
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# create a mask for our object
	masked_frame = cv2.inRange(hsv_frame, lowerThresh, upperThresh)

	# we erode to eat away small bits
	eroded = cv2.erode(masked_frame, None, iterations=2)
	# we dilate to fill the holes
	dilated = cv2.dilate(eroded, None, iterations=0)

	# to get the object now, we find the contours in the image
	contours, heirarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	# for those contours, a rectangle around it

	if(len(contours)==0 and repeatCondition):
		stack.append([])
		repeatCondition = False

	for contour in contours:
		(x,y,w,h) = cv2.boundingRect(contour)

		# to avoid small noise, an area filter
		if((w*h) > areaThreshold):
			repeatCondition = True
			# draw a rectangle for detection
			#            -frame- -start-   -end-    -color-  -thickness-
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
			# add point to draw (add to stack's top)
			try: # this exception handling is to handle the synchronization issues
				stack[-1].append((x,y))
			except:
				pass

	# now time to draw points
	# this time, we use a stack
	# each stack element is a continuous line to be displayed
	for temp in stack:
		for i in range(len(temp)):
			point1 = temp[i]
			try:
				point2 = temp[i+1]
			except:
				point2 = point1
			cv2.line(frame, point1, point2, color_var, 3)
			cv2.line(canvas, point1, point2, color_var, 3)

	# flip vertically for better viewing
	flipped_frame = cv2.flip(frame, 1)
	flipped_canvas = cv2.flip(canvas, 1)

	# show the final image
	cv2.imshow('output-window', frame)
	cv2.imshow('canvas', canvas)

	# if A is pressed, then screen is cleared
	if(keyboard.is_pressed('a')):
		stack = []

	# some inputs for changing drawing colour
	if(keyboard.is_pressed('r')):
		color_var = (0,0,255)
	if(keyboard.is_pressed('g')):
		color_var = (0,255,0)
	if(keyboard.is_pressed('b')):
		color_var = (255,0,0)

	# to exit window, press Q
	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break

# finally release and destroy window
cap.release()
cv2.destroyAllWindows()