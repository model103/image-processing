import os
import numpy as np

object_line1 = 'y = '  #检测字段
long = 7  #字段后数据长度
object_len1 = len(object_line1)

file = open("D:\OneDrive - stu.hit.edu.cn\E盘\img_ShapeBasedMatching/noise_img/noise_0.5/result.txt")
txt = file.read()
txt_len = len(txt)

key = []
for i in range(txt_len - object_len1):
    if txt[i:i + object_len1] == object_line1:
        print(txt[i + object_len1:i + object_len1 + long])  # 往后long个字符就是耗时时间了
        key.append(txt[i + object_len1:i + object_len1 + long])

print("检测到样本数：", len(key))
#print(key)
#print("匹配时间均值：", np.mean(GAD_time))
#print("匹配时间相对标准差：", np.std(GAD_time) / np.mean(GAD_time))  # RSD
