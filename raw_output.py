import cv2
import pytesseract

# refer exe file
pytesseract.pytesseract.tesseract_cmd = 'path-to-tesseract.exe'
# sample path--->E:\\Tesseract-OCR\\tesseract.exe

img = cv2.imread('data.jpg')

# pytessaract accepts only RGB value but cv2 accepts only BGR. So convert it before we send into pytesseract library
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#for raw imformation
print(pytesseract.image_to_string(img))

# ONLY for location of character and box making---> Gives each character (x,y,w,h) coordinate values
print(pytesseract.image_to_boxes(img))

#output will occur on console

cv2.imshow('result',img)
cv2.waitKey(0)
