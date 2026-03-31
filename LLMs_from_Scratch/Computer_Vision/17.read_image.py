import cv2

# read an image
img1 = cv2.imread('bus.jpg')

# Check if image loaded successfully
if img1 is None:
    print("Error: Image not found. Check the file path.")
else:
    cv2.imshow('The Original Image', img1)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

# save image to a file
cv2.imwrite('save_img1.jpg', img1)    