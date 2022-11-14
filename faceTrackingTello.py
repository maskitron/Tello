from utlis import *
import cv2

w = 360
h = 240

pid = [0.5, 0.5, 0]
pError = 0
startCounter = 0 # for no flight 1 , 0 for flight


myDrone = initTello()


while True:
    ## Flight
    if startCounter ==0:
        myDrone.takeoff()
        startCounter = 1




    img = telloGetFrame(myDrone, w, h)

    img, info = findFace(img)

    pError = trackFace(myDrone, info, w, pid, pError)


    print(info[0][0])


    cv2.imshow('Image',img)

    if cv2.waitKey(1)& 0xFF == ord('q'):
        myDrone.land()
        break