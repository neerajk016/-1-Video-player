import cv2
im=input("enter the image")
# im="pic1.jpg"
img_file=im
classifier_file="car_classifier.xml"
img=cv2.imread(img_file)
black_n_white=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
car_tracker=cv2.CascadeClassifier(classifier_file)
cars=car_tracker.detectMultiScale(black_n_white)
for(x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
cv2.imshow("Neeraj",img)
cv2.waitKey()


