import numpy as np
# import matplotlib.pyplot as plt


a=np.array([[1,2],[4,5],[7,8]])
b=np.zeros((2,3))

print(np.unravel_index(a.argmax(),a.shape))

