import urllib
import urllib2
import cv2
import numpy
import os

def store_raw_images():
    img_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04373704'
    img_urls = urllib2.urlopen(img_link).read()

    if not os.path.exists('chair'):
        os.makedirs('chair')

    pic_num = 1

    for i in img_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i,"pos/" + str(pic_num) + '.jpg')
            img = cv2.imread("chair/"+str(pic_num)+'.jpg')
            pic_num += 1

        except Exception as e:
            print (str(e))

store_raw_images()