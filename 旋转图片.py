from math import *
import cv2
import os
import glob
import numpy as np

def rotate_img(img, angle):
    '''
    img   --image
    angle --rotation angle
    return--rotated img
    '''
    h, w = img.shape[:2]
    rotate_center = (w/2, h/2)
    #获取旋转矩阵
    # 参数1为旋转中心点;
    # 参数2为旋转角度,正值-逆时针旋转;负值-顺时针旋转
    # 参数3为各向同性的比例因子,1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
    M = cv2.getRotationMatrix2D(rotate_center, angle, 1.0)
    print(M)
    #计算图像新边界
    new_w = int(h * np.abs(M[0, 1]) + w * np.abs(M[0, 0]))
    new_h = int(h * np.abs(M[0, 0]) + w * np.abs(M[0, 1]))
    #调整旋转矩阵以考虑平移
    M[0, 2] += (new_w - w) / 2
    M[1, 2] += (new_h - h) / 2

    rotated_img = cv2.warpAffine(img, M, (new_w, new_h))
    constant = np.array([0.0,0.0,0.0])
    rotated_img_pad = a = cv2.copyMakeBorder(rotated_img,100,100,100,100,cv2.BORDER_CONSTANT,value=[0,0,0])
    (h1,w1,z1) = rotated_img_pad.shape
    print(h1,w1)
    #print(h//2-240,h//2+240,w//2-320,w//2+320)
    rotated_cut_img = rotated_img_pad[h1//2-h/2:h1//2+h//2,w1//2-w//2:w1//2+w//2,:]
    #print(rotated_cut_img)
    return rotated_cut_img


image = cv2.imread("11.bmp", -1)
        ##方法1
rotated_img1 = rotate_img(image, 1)
        #basename = os.path.basename(image_name)
        #tag, _ = os.path.splitext(basename)
cv2.imwrite("rotated_img/1.bmp", rotated_img1)
