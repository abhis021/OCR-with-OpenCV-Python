import cv2
import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('test.jpg')
img = cv2.resize(img, (500, 500))

cv2.imshow('image', img)
text = pyt.image_to_string(img)
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()