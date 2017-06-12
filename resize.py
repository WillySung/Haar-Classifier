import cv2
import os

images = []
for filename in os.listdir('chair'):
        img = cv2.imread(os.path.join('chair',filename))
        resized_img = cv2.resize(img,(50,50))
        cv2.imwrite('chair/resized_'+filename,resized_img)
