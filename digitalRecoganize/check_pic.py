import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab
import sys

inputData = pd.read_csv('train.csv')


image_num = int(sys.argv[1])
print(image_num)
temp = np.array(inputData.iloc[image_num][1:]).reshape(28,28)
plt.imshow(temp)
plt.show()
