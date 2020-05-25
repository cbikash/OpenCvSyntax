import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#read the input image
#img = cv2.imread('lena.jpg')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img= cap.read()

    img1= cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img1,1.1,8)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()