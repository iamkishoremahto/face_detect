import cv2

img= cv2.imread('lena.jpg',-1)
cv2.imshow('image',img)
key = cv2.waitKey(0)

if key == 27 :
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lena_copy.jpg',img)
    cv2.destroyAllWindows()
# print(img)