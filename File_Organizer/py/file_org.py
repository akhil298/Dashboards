import cv2 as cv2

capture=cv.VideoCapture(0)
ret,frame= capture.read()

for i in range(100):
    ret, frame = capture.read()
    cv.imwrite('dsfs',frame)

cv.destroyAllWindows()
cv.release()