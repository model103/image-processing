import os
import numpy as np

result_path = 'D:\GAD_template_matching\Results/'
result_names = os.listdir(result_path)
#删除非txt文件
temp = result_names.copy()
for file in temp:
    if '.txt' not in file: result_names.remove(file)

#GAD的result文件是按一下排序的
name_order = os.listdir("../supplementary_experiment/noise_img/noise_0/")
for i, name in enumerate(name_order):
    name_order[i] = int(name.split('.')[0])
print(name_order)


t_col = [269
,365
,360.3014256
,346.6656315
,325.4273842
,298.6656315
,269
,239.3343685
,212.5726158
,191.3343685
,177.6985744
,173
,177.6985744
,191.3343685
,212.5726158
,239.3343685
,269
,298.6656315
,325.4273842
,346.6656315
,360.3014256
]

t_row= [190
,190
,219.6656315
,246.4273842
,267.6656315
,281.3014256
,286
,281.3014256
,267.6656315
,246.4273842
,219.6656315
,190
,160.3343685
,133.5726158
,112.3343685
,98.69857444
,94
,98.69857444
,112.3343685
,133.5726158
,160.3343685
]

#读取GAD结果文本
p_col = []
p_row = []
for result_name in result_names:
    file = open(result_path + result_name)
    txt_lines = file.readlines()
    col = (int(txt_lines[0]) + int(txt_lines[2]) - 1) /2
    p_col.append(col)
    row = (int(txt_lines[1]) + int(txt_lines[3]) - 1) / 2
    p_row.append(row)

#计算检测精度，平均误差，std
error = []
for i in range(21):
    error.append(((p_col[i]-t_col[name_order[i]])**2 + (p_row[i]-t_row[name_order[i]])**2)**0.5)  #按文件读取循序排列的error
print(error)
#print('mean_error', np.mean(error))
#print('std_error', np.std(error))