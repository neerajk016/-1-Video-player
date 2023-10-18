import cv2
im=(input("enter the image name"))
img_file=im
img=cv2.imread(img_file)
cv2.imshow("Neeraj",img)
cv2.waitKey()
