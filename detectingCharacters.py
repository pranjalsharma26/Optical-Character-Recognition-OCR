import cv2
import pytesseract

# refer exe file
pytesseract.pytesseract.tesseract_cmd = 'path-to-tesseract.exe'

img = cv2.imread('data.jpg')

# pytessaract accepts only RGB value but cv2 accepts only BGR. So convert it before we send into pytesseract library
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

h_img,w_img,_=img.shape # parameters-> h,w,channels---takes the image shape
boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    print(b)
    b= b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    # height is opposite to x, so subtarct h from y and do not add(normally we add)
    cv2.rectangle(img,(x,h_img-y), (w,h_img-h), (0,0,255), 3)
    # label around box
    cv2.putText(img,b[0],(x,h_img-y+30), cv2.FONT_ITALIC,1,(23,45,233),2)

cv2.imshow('result',img)
cv2.waitKey(0)
