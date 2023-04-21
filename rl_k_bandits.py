'''
k-bandits simulation
you can do this in O-O, functional, or imperative style
I used imperative here

'''
import numpy as np
import random as rnd

e = .01
k = 10  # number of bandits
q_star = np.zeros([k])
rewards = [rnd.uniform(0,100) for _ in range(k)]
counts = np.zeros([k])



r_total = 0  # total rewards

def init_bandits():
    for i in range(k):
        q_star[i] = rnd.gauss(0, 1)


def run_bandits(n_steps):
    for i in range(n_steps):
        for i in range(k):
            a = rnd.choices([rnd.choice(np.flatnonzero(q_star == q_star.max())), rnd.randint(0,k-1)], weights=((1-e),e))[0]
            print(a)
            counts[a] += 1
            q_star[a] = q_star[a] + (1/counts[a]) * (rewards[a] - q_star[a])


if __name__ == '__main__':
    rnd.seed(rnd.randint(0,1000))
    init_bandits()
    x = run_bandits(1000)

    for i in range(k):
        print("estimate: ", q_star[i], "     true value: ", rewards[i])