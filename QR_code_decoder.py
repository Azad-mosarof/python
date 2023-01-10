import cv2 
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('QR1.png')
img = cv2.resize(img,(500,500))

code  = decode(img)

for barcode in code:
    print(barcode.data)
    text = barcode.data.decode('utf-8')
    print(text)
    print(barcode.rect[2])
    x,y,w,h = barcode.rect[0],barcode.rect[1],barcode.rect[2],barcode.rect[3]
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.putText(img,text,(50,25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),1)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()