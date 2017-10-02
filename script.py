import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("aamir.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image in grey",gray_img)
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors =5)
# Creating rectangle shape cascade
for x,y,h,w in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized_image = cv2.resize(img, (int(img.shape[1]),int(img.shape[0])))

print(type(faces))
cv2.imshow("Gray",resized_image)
print(faces)
cv2.waitKey(0)
cv2.destroyAllWindows()