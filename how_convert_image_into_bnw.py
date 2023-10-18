import cv2
im=(input("enter the image name"))
# im="pic1.jpg"
img_file=im
img=cv2.imread(img_file)
black_n_white=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Neeraj",black_n_white)
cv2.waitKey()
