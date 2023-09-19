import numpy as np
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

#读检测值
file = open("D:\OneDrive - stu.hit.edu.cn\E盘\python/supplementary_experiment/Lu的结果/move_illumination_0.8 400.txt")
txt_lines = file.readlines()
pd_col = []
pd_row = []
for line in txt_lines:
    split = line.split(' ')
    pd_col.append(float((split[0])))
    pd_row.append(float((split[-1]).replace('\n','')))
pd_col = np.array(pd_col)
pd_row = np.array(pd_row)

#计算mean_error, std
error = np.sqrt((true_row - pd_row)**2 + (true_col - pd_col)**2)
print(error)
print(np.mean(error))
print(np.std(error))


