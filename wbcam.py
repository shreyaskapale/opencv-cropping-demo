import cv2
photo=cv2.imread("img.jpg")
x,y = input("Enter the cropping dimensions x and y : ").split()
new_img=photo[y:x]
while True:
    cv2.imshow("img",new_img)
    if cv2.waitKey(0) & 0xFF==ord('s'):
        filename = input("Enter the filename to save the cropped image")
        cv2.imwrite(filename, new_img) 
        break
cv2.destroyAllWindows()      

