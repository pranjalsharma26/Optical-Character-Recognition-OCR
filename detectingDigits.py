import cv2
import pytesseract

# refer exe file
pytesseract.pytesseract.tesseract_cmd = 'path-to-tesseract.exe'

img = cv2.imread('data.jpg')

# pytessaract accepts only RGB value but cv2 accepts only BGR. So convert it before we send into pytesseract library
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

h_img,w_img,_=img.shape
con = r'--oem 3 --psm 6 outputbase digits'
# oem-engine stuff and see documentation
boxes = pytesseract.image_to_data(img, config=con)
print(boxes)
# Various data is coming in column and unwanted 1st row as well..so to eliminate it->
for x,b in enumerate(boxes.splitlines()):
    #print(b)
    if x!=0:
        b= b.split()
        print(b)    # the data part has 12 elements in the list
        if(len(b)==12):
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (w+x,h+y), (0, 0, 255), 3)
            cv2.putText(img,b[11],(x,y), cv2.FONT_ITALIC,1,(23,45,233),2)

cv2.imshow('result',img)
cv2.waitKey(0)
