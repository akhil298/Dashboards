import cv2 as cv



#initializing the camera
image=cv.VideoCapture(0)

#until the condition 
while True:

    #ret indicated the bool value if the video is recording then it is true
    ret,frame=image.read()

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    cv.imshow('the current window',frame)
    cv.waitKey(55)

image.release()
out.release()
cv.destroyAllWindows()