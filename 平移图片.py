import cv2 as cv
import numpy as np
'''
image = cv.imread('../supplementary_experiment/illumination_img\ill_0.8/400 0.8.bmp')

rows,cols=image.shape[:2]
tx=298.66563146-269
ty=281.30142556-190

tx = np.array([269
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
]) - 269

ty = np.array([190
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
]) - 190

for i in range(21):
    moving_matrix=np.float64([[1,0,tx[i]],[0,1,ty[i]]])
    image_move=cv.warpAffine(image,moving_matrix,(cols,rows))
    cv.imwrite('../supplementary_experiment/illumination_img/ill_0.8/'+str(i)+'.bmp',image_move)

'''