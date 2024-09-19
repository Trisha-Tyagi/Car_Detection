import cv2
cap=cv2.VideoCapture("./CarDetection/video2.mp4")
while True:
    r,f=cap.read()
    if r == True:
        f=cv2.resize(f,(1000,750))
        gry=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
        gry=cv2.resize(gry,(1000,750))
        car=cv2.CascadeClassifier("./CarDetection/car.xml")
        cars=car.detectMultiScale(gry,1.1,10)
        for (x,y,w,h) in cars:
            cv2.rectangle(f,(x,y),(x+w,y+h),(0,0,255),3)

        cv2.imshow("ws",f)
        if cv2.waitKey(10) & 0xff==ord("p"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
