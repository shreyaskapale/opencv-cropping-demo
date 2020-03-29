import cv2
photo=cv2.imread("img.jpg")
new_img=photo[100:240]
while True:
    cv2.imshow("img",new_img)
    if cv2.waitKey(0) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()      

