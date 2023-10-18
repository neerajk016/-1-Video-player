import cv2
#our image
img_file="cars.jpg"

#our video
video=cv2.VideoCapture("video1.mp4")


classifier_file="car_classifier.xml"
pedestria_file="human_classifier.xml"


car_tracker=cv2.CascadeClassifier(classifier_file)



pedestrian_tracker=cv2.CascadeClassifier(pedestria_file)

# run forever until car stops

while True:
    
    #Reading the currebt frame
    (read_sucessfull,frame)=video.read()


    #safecoding
    if read_sucessfull:
        #coverting to grayscale
        grayscaled_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break  
    #detecting cars
    cars=car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians=pedestrian_tracker.detectMultiScale(grayscaled_frame)


    for (x,y,w,h) in cars:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,225),2)

    for(x,y,w,h) in pedestrians:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,225),2)




    



    cv2.imshow("Neerajk",frame) 
    key=cv2.waitKey(1)   




    #stop if q is resssed
    if key==81 or key==113:
        break

#releasw vieocapture object
video.release()


print(len(cars))
print(len(pedestrians))













"""


#our classifier file
classifier_file="car_classifier.xml"


#Reading colorimage
img=cv2.imread(img_file)


#changing color to bndw
black_nd_white=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#taking classififer file
car_tracker=cv2.CascadeClassifier(classifier_file)


#detecting cars

cars=car_tracker.detectMultiScale(black_nd_white)


#drawing rectangle in cars
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),3)




#showing image
cv2.imshow("car tracker",img)
cv2.waitKey()
"""



