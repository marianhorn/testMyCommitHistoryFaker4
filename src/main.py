import math
import numpy
import matplotlib.pyplot as plt
import brownian as bm
import random
"""
High-frequency trading in a limit order book, Marco Avellaneda & Sasha Stoikov
paper url: https://www.researchgate.net/publication/24086205_High_Frequency_Trading_in_a_Limit_Order_Book

Some model limitations, discussed: https://quant.stackexchange.com/questions/36400/avellaneda-stoikov-market-making-model
Parameter fitting: https://quant.stackexchange.com/questions/36073/how-does-one-calibrate-lambda-in-a-avellaneda-stoikov-market-making-problem
"""

##########################################
#       Simulations
#########################################

n_sim = 100

pnl_sim = numpy.empty((n_sim))

for i_sim in range(n_sim):

    ##########################################
    #       Stock price
    #########################################

    # The Wiener process parameter.
    sigma = 2
    # Total time.
    T = 1.0
    # Number of steps.
    N = 200 # int(T/dt)
    # Time step size
    dt = T/N # 0.005
    # Create an empty array to store the realizations.
    s = numpy.empty((N+1))
    # Initial value of x.
    s[0] = 100

    bm.brownian(s[0], N, dt, sigma, out=s[1:])

    t = numpy.linspace(0.0, N*dt, N+1)

    # plt.plot(t, s)
    # plt.xlabel('time', fontsize=16)
    # plt.ylabel('price', fontsize=16)
    # plt.grid(True)
    # plt.show()

    ##########################################
    #       Computational loop
    #########################################

    # Limit horizon
    limit_horizon = True

    # Wealth
    pnl = numpy.empty((N+2))
    pnl[0] = 0

    # Cash
    x = numpy.empty((N+2))
    x[0] = 0

    # Inventory
    q = numpy.empty((N+2))
    q[0] = 0
    q_max = 10

    # Risk factor (->0: high risk, ->1: low risk)
    gamma = 0.1

    # Market model
    k = 1.5

    # Reserve price
    r = numpy.empty((N+1))

    # Optimal quotes
    ra = numpy.empty((N+1))
    rb = numpy.empty((N+1))

    # Order consumtion probability factors
    M = s[0]/200
    A = 1./dt/math.exp(k*M/2)

