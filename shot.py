import cv2

cam = cv2.VideoCapture(0)  
img_counter=1
while (True):
    s, img = cam.read()
    if s:  
        cv2.imshow("cam-test",img)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_name = "pen/frame_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, img)
            print("{} written!".format(img_name))
            img_counter += 1

cv2.destroyWindow("cam-test")
    