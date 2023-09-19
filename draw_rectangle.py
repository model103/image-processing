import cv2

height = 93  #模板大小
width = 94
width = 94
image = cv2.imread('occlusion_img/occlusion_0.02_53.bmp')


#画our结果
c_row = 255.025    #目标框中心位置
c_col = 414.149
cv2.rectangle(image, (round(c_col-width/2), round(c_row-height/2)), (round(c_col+width/2), round(c_row+height/2)), (0,0,255), 2)  #(col,row)  #红色
#画NCC结果
c_row = 257.5   #目标框中心位置
c_col = 415.0
cv2.rectangle(image, (round(c_col-width/2), round(c_row-height/2)), (round(c_col+width/2), round(c_row+height/2)), (0,255,0), 2)  #(col,row) #绿色
#画GAD结果
cv2.rectangle(image, (369, 207), (463,300), (252,21,4), 2)  #(col,row)   #蓝色

#画SB结果
c_row = 256.578161   #目标框中心位置
c_col = 414.065724
cv2.rectangle(image, (round(c_col-width/2), round(c_row-height/2)), (round(c_col+width/2), round(c_row+height/2)), (0,255,255), 2)  #(col,row), 黄色

cv2.imwrite('occlusion_img/our_NCC_SB_GAD_0.02.bmp', image)

'''
367.513657   576.017533
174 COL
106 ROW
268
199

343
206
437
299
367.513657   576.017533
x = 414.743  y = 254.745
OUR (0,0,255)
NCC (252,21,4)
'''