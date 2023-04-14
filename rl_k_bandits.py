'''
k-bandits simulation
you can do this in O-O, functional, or imperative style
I used imperative here

'''
import numpy as np
import random as rnd

k = 10  # number of bandits
q_star = np.zeros([k])
rewards = np.zeros([k])
counts = np.zeros([k])



r_total = 0  # total rewards

def init_bandits():
    for i in range(k):
        q_star[i] = rnd.gauss(0, 1)


def run_bandits(n_steps):
    for i in range(n_steps):
        counts[0] += 1


if __name__ == '__main__':
    rnd.seed(42)
    init_bandits()
    x = run_bandits(1000)

    for i in range(k):
        print(q_star[i])