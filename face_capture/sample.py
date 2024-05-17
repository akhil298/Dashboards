import cv2 as cv

'image=cv.VideoCapture(0)'
array_data=[]
'''while True:
    ret, frame=image.read()
    cv.imshow('frame',frame)
    if cv.waitKey(2) & 0xff ==ord('c'):
        break
       # array_data.append(frame)
    else:
        cv.waitKey(1) & 0xff ==ord('b')
        array_data.append(frame)
cv.destroyAllWindows()
image.release()

'''
print(len(array_data))