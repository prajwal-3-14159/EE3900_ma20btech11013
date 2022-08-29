import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

# If using termux
# import subprocess
# import shlex
#
# end if


x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
k = 20
y = np.zeros(k)

y[0] = x[0]
y[1] = -0.5 * y[0] + x[1]

for n in range(2, k - 1):
    if n < 6:
        y[n] = -0.5 * y[n - 1] + x[n] + x[n - 2]
    elif 5 < n < 8:
        y[n] = -0.5 * y[n - 1] + x[n - 2]
    else:
        y[n] = -0.5 * y[n - 1]
print(y)
print(len(y))
# subplots
plt.subplot(2, 1, 1)
plt.stem(range(0, 6), x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()  # minor

#np.savetxt("./prob-3-1.txt", y)

plt.subplot(2, 1, 2)
plt.stem(range(0, k), y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()  # minor

# If using termux
plt.savefig('../figs/prob_3-1.eps')
plt.savefig('../figs/prob_3-1.png')
plt.savefig('../figs/prob_3-1.pdf')
# subprocess.run(shlex.split("termux-open ../figs/xnyn.pdf"))
plt.show()
