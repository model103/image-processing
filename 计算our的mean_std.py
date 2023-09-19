import numpy as np
import os
#读真值
file = open("D:\OneDrive - stu.hit.edu.cn\E盘\python/supplementary_experiment/Lu的结果/accurate_position.txt")
txt_lines = file.readlines()
true_col = []
true_row = []
for line in txt_lines:
    split = line.split(' ')
    true_col.append(float((split[0])))
    true_row.append(float((split[-1]).replace('\n','')))
true_col = np.array(true_col)
true_row = np.array(true_row)

#读取检测值
long = 7  #字段后数据长度
object_line1 = 'x = '  #检测字段
object_len1 = len(object_line1)

file = open("../supplementary_experiment/illumination_img/result/our_result/ill_0.8.txt")
txt = file.read()
txt_len = len(txt)

pd_col = []
for i in range(txt_len - object_len1):
    if txt[i:i + object_len1] == object_line1:
        #print(txt[i + object_len1:i + object_len1 + long])  # 往后long个字符就是耗时时间了
        pd_col.append(float(txt[i + object_len1:i + object_len1 + long]))
pd_col = np.array(pd_col)

object_line1 = 'y = '  #检测字段
object_len1 = len(object_line1)
pd_row = []
for i in range(txt_len - object_len1):
    if txt[i:i + object_len1] == object_line1:
        #print(txt[i + object_len1:i + object_len1 + long])  # 往后long个字符就是耗时时间了
        pd_row.append(float(txt[i + object_len1:i + object_len1 + long]))
#pd_row = np.array(pd_row)

#看看读片读取顺序,并重排序
name_order = os.listdir("../supplementary_experiment/illumination_img/ill_0/")
for i, name in enumerate(name_order):
    name_order[i] = int(name.split('.')[0])
pd_col = np.array([i for _,i in sorted(zip(name_order,pd_col))])  #把name_order排序，pd_col按相同顺序排序
pd_row = np.array([i for _,i in sorted(zip(name_order,pd_row))])


#计算mean_error, std
error = np.sqrt((true_row - pd_row)**2 + (true_col - pd_col)**2)
print(error)
print(np.mean(error))
print(np.std(error))
