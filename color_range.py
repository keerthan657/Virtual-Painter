import cv2
import numpy as np

def callback(x):
	pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('capture')

lowH = lowS = lowV = 0
upH = 179
upS = upV = 255

cv2.createTrackbar('lowH', 'capture', lowH, 179, callback)
cv2.createTrackbar('upH', 'capture', upH, 179, callback)
cv2.createTrackbar('lowS', 'capture', lowS, 255, callback)
cv2.createTrackbar('upS', 'capture', upS, 255, callback)
cv2.createTrackbar('lowV', 'capture', lowV, 255, callback)
cv2.createTrackbar('upV', 'capture', upV, 255, callback)

while(True):
	ret, frame = cap.read()

	# retFrame = frame-operations
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lowH = cv2.getTrackbarPos('lowH', 'capture')
	upH = cv2.getTrackbarPos('upH', 'capture')
	lowS = cv2.getTrackbarPos('lowS', 'capture')
	upS = cv2.getTrackbarPos('upS', 'capture')
	lowV = cv2.getTrackbarPos('lowV', 'capture')
	upV = cv2.getTrackbarPos('upV', 'capture')

	lower_hsv = np.array([lowH, lowS, lowV])
	upper_hsv = np.array([ upH,  upS,  upV])
	mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

	cv2.imshow('capture', hsv)
	cv2.imshow('masked', mask)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()