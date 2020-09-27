import matplotlib.pyplot as plt
import numpy as np

for i in range(10,15):
    x=np.linspace(0,i,11)
    y=np.linspace(0,i,11)

    plt.figure()
    plt.plot(x,y)
    plt.xlabel("x轴")
    plt.ylabel('y轴')
plt.show()
