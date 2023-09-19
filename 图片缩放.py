import cv2
import numpy as np

img1 = cv2.imread("../paper_images/scale/100.bmp", 0)  # 只能相对路径？


def img_resize(img, scale):  # 将图片缩放到scal被，然后格式化成原图大小（补黑边或剪裁）
    th, tw = img.shape  # 先高后宽
    new_img_tmp = cv2.resize(img, (int(tw * scale), int(th * scale)))  # 先宽后高

    if scale < 1:
        new_img = np.zeros((th, tw))
        up = (th - int(th * scale)) // 2  # 上方黑边宽度
        left = (tw - int(tw * scale)) // 2  # 左边黑边宽度
        new_img[up:up + int(th * scale), left:left + int(tw * scale)] = new_img_tmp
    else:
        up = (int(th * scale) - th) // 2  # 上方裁掉的宽度
        left = (int(tw * scale) - tw) // 2  # 上方裁掉的宽度
        new_img = new_img_tmp[up:up + th, left:left + tw]
    return new_img


for i in np.arange(0.8, 1.21, 0.02):
    new_img = img_resize(img1, i)
    cv2.imwrite("../paper_images/scale_new/"+str(int(i*100))+".bmp", new_img)