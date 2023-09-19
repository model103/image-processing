from shutil import copyfile
import os

source = 'D:/GAD_template_matching/Template/template.bmp'
target_flod = 'D:/GAD_template_matching/SAL_mask100/'  #SAL_mask100 Template

img_names = os.listdir('D:\GAD_template_matching\Target')

for name in img_names:
    target_name = target_flod + name
    copyfile(source, target_name)