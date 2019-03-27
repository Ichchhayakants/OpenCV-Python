import cv2
import numpy as np 

cap = cv2.VideoCapture(0)


while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #hue saturation value


	lower_red = np.array([0,50,50])
	upper_red = np.array([180,255,255])

	#dark_red = np.unit8([[[12,22,121]]])
	
	mask = cv2.inRange(hsv,lower_red,upper_red)
	result = cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('result', result)

	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break

cv2.destroyAllwindows()
cap.release()