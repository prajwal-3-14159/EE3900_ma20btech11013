import matplotlib.pyplot as plt

X = [1, 1]
Y = [1]
for i in range(20):
    n = X[i] + X[i+1]
    X.append(n)

for i in range(1, 21):
    m = X[i-1] + X[i+1]
    Y.append(m)

#plt.plot(X)
plt.stem(range(len(Y)), Y)
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.tight_layout()
plt.savefig('../figs/prob_2-5.pdf')
plt.savefig('../figs/prob_2-5.eps')
plt.savefig('../figs/prob_2-5.png')
plt.show()
