import cv2 as cv
x0 = 400
y0 = 465
#x0 = 269  #中心处坐标
#y0 = 190
l = 151
img = cv.imread('../..\img_ShapeBasedMatching/rotated_img/11.bmp')
print(img.shape)
cropped = img[int(y0-l//2):int(y0+(l+1)//2),int(x0-l//2):int(x0+(l+1)//2),:]
cv.imwrite('../../img_ShapeBasedMatching/rotated_img/template.bmp',cropped)

