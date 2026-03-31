import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8)

# Draw a blue line (255,0,0) on Canvas (startpoint(0,0), endpoint(511,511), color(255,0,0), thickness(5)
cv2.line(canvas, (0,0), (511,511), (255,0,0), 15)  

# draw a green rectangle on canvas   
cv2.rectangle(canvas, (384,0), (510,128), (0,255,0), -1)

# write white text on canvas
cv2.putText(canvas, 'OpenCV  Practice', (10,500), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

cv2.imshow('Canvas with Shape', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
