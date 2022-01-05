import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7,3])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)
a7 = np.arange(0, 10, 0.02)

2*a1

1/a1

1/a1 + a1 + 2

x = np.linspace(0, 1, 100)
y = x**2

plt.plot(x, y)
plt.show()

plt.hist(a4)
plt.show()

def f(x):
    return x**2 * np.sin(x) / np.exp(-x)
x = np.linspace(0, 10, 100)
y = f(x)

plt.plot(x, y)
plt.show()

a1 = np.array([2,4,6,8,10])

a1[2]

a1[2:]

a1[:-2]

a1[1:-2]

a1[a1>3]

names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
names[first_letter_j]

a1%4

a1%4==0

a1[a1%4==0]