import numpy as np
x0 = 400
y0 = 465
r = np.sqrt((x0-512)**2+(y0-384)**2)

theta = np.arctan((y0-384)/(512-x0))
theta1 = theta + np.deg2rad(1)
print(np.rad2deg(theta))
x1 = 512 - r*np.cos(theta1)
y1 = 384 + r*np.sin(theta1)
print(x1,y1)
