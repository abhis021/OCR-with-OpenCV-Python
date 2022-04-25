import cv2
import pytesseract as pyt
#declaring path of tesseract installation
pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#declaring image file
img = cv2.imread('test.jpg')
# img = cv2.resize(img, (1366, 768))

# showing image file
cv2.imshow('image', img)

#declaring text variable that converts image to text
text=pyt.image_to_string(img, lang='hin')
#prints text for preview in terminal
print(text)

# This writes the result to a text file
with open('file.txt', mode='w') as f:
    f.write(text)

#standard waitKey method
cv2.waitKey(0)
cv2.destroyAllWindows()