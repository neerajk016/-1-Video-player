import cv2
vi=input("enter the video name")
video=cv2.VideoCapture(vi)
while True:
    (read_sucessfull,frame)=video.read()
    cv2.imshow("Neeraj",frame)
    cv2.waitKey(0)
