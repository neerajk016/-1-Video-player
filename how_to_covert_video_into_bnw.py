import cv2
vi=input("enter the video name")
video=cv2.VideoCapture(vi)
while True:
    (read_sucessfull,frame)=video.read()
    if read_sucessfull:
        grayscaled_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    else:
        break
    cv2.imshow("Neeraj",grayscaled_frame)
    cv2.waitKey()
