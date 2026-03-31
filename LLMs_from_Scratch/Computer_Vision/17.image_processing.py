import cv2

img = cv2.imread('bus.jpg')

resize = cv2.resize(img, (640,480))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurring = cv2.GaussianBlur(img, (5,5), 0)   # blurring is done with filters (5,5)
edges = cv2.Canny(img, 100,200)     #Canny edge detector for pixel manipulation (100 by 200)

cv2.imshow('Resize', resize)
cv2.imshow('Grey Image', grey)
cv2.imshow('Blurring Image', blurring)
cv2.imshow('Edges Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()