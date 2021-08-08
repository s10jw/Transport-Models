import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import math


"""
This file aims to aid in my understanding of working with Quantum Mechanics numerically instead of analytically as I 
have before. I begin by calculating the eigenvalues of a harmonic oscillator and infinite square well.
"""

""" Initializations """
a = -5  #float(input('Enter lower limit of domain: '))
b = 5  #float(input('Enter upper limit of domain: '))
N = 100  #int(input('Enter number of states: '))

funcType = int(input('Would you like to see: \n1. Eigenvectors (Wavefunctions)\n2. Probability Distributions\n'))

found = False

while found is False:
    if funcType == 1:
        def funcReturn(x):
            """ Takes in a wavefunction, returns the same wavefunction """
            return x
        found = True
    elif funcType == 2:
        def funcReturn(x):
            """ Takes in a wavefunction, returns the probability distribution of that wavefunction """
            return x**2
        found = True
    else:
        print('This is not an allowed input, please try again.')
        funcType = int(input('Would you like to see: \n1. Eigenvectors\n2. Probability Distributions\n'))

vType = int(input('Choose a potential: \n1. Infinite Square Well\n2. Harmonic Oscillator\n'))

found = False

while found is False:
    if vType == 1:
        def vFunc(x):
            """ Takes in a position, returns the potential at that position for an ISW """
            return 0
        found = True
    elif vType == 2:
        def vFunc(x):
            """ Takes in a position, returns the potential at that position """
            return x ** 2
        found = True
    else:
        print('This is not an allowed input, please try again.')
        vType = int(input('Choose a potential: \n1. Infinite Square Well\n2. Harmonic Oscillator\n'))


if funcType == 1 and vType == 1:
    title = 'Eigenvectors for an Infinite Square Well using Finite Difference Method'
elif funcType == 1 and vType == 2:
    title = 'Eigenvectors for a Harmonic Oscillator using Finite Difference Method'
elif funcType == 2 and vType == 1:
    title = 'Probability Distribution for an Infinite Square Well using Finite Difference Method'
elif funcType ==2 and vType == 2:
    title = 'Probability Distribution for an Infinite Square Well using Finite Difference Method'

""" Computational Parameters """
x = np.array(np.linspace(a, b, N))
h = x[1] - x[0]

""" Potential Energy Function """



def vHO(x):
    """ Takes in a position, returns the potential at that position """
    return x**2

""" Hamiltonian Formation """
KE = np.zeros((N-2, N-2))
for i in range(N-2):
    for j in range(N-2):
        if i == j:
            KE[i, j] = -2
        elif np.abs(i - j) == 1:
            KE[i, j] = 1
        else:
            KE[i, j] = 0

""" Potential Energy Matrix """
V = np.zeros((N-2,N-2))
for i in range(N - 2):
    V[i, i] = vFunc(x[i + 1])

""" Eigenvalue Calculations """
H = -KE / (2*h**2) + V

val, vec = np.linalg.eig(H)
z = np.argsort(val)
z = z[0:4]
for i in range(len(z)):
    print(val[z[i]])

""" Plot Eigenvectors """
plt.figure(figsize=(10,12))
for i in range(len(z)):
    y = []
    y = np.append(y, vec[:, z[i]])
    y = np.append(y, 0)
    y = np.insert(y, 0, 0)
    plt.plot(x, funcReturn(y), lw=3, label="{} ".format(i))
    plt.xlabel('x', size=14)
    plt.ylabel('$\psi$ (x)', size=14)
plt.legend()
plt.title(title, size=14)
plt.show()




