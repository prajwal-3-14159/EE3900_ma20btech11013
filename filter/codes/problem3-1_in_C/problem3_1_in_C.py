import numpy as np
import matplotlib.pyplot as plt

k = 20

f = open('./arr_x.txt', 'r')
lines = f.readlines()

arr_y = np.array(list(map(float, lines[0].split(" ")[:-1])))

print(arr_y)
print(len(arr_y))

plt.subplot(2, 1, 2)
plt.stem(range(0, k), arr_y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()  # minor

plt.savefig("xnyn_c.pdf")
plt.show()
f.close()