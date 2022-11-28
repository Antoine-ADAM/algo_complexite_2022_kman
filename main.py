import numpy as np
import matplotlib.pyplot as plt
import kman

# generate random data
X = np.r_[np.random.randn(15, 2) + [3, 3], np.random.randn(15, 2) + [2, -2], np.random.randn(15, 2) + [-2, 2]]

res = kman.kman(kman.Point.from_list(X), 3)
hexa = '0123456789ABCDEF'
for e in res:
    plt.scatter(e[0][0], e[0][1], c="red")
    color = '#' + hexa[np.random.randint(0, 5)] + hexa[np.random.randint(0, 15)] + hexa[np.random.randint(0, 15)]
    for p in e[1]:
        plt.scatter(p[0], p[1], c=color)
plt.show()