

import numpy as np
from pylab import *


class neuron_Izhi_model:
    def __init__(self):
        self.dt = 0.01
        self.n_steps = 10000
        self.a = 0.02
        self.b = 0.2
        self.c = -55
        self.d = 2
        self.u = np.zeros((n_steps))
        self.v = np.zeros((n_steps))
        self.v[0] = -65
        self.I_in = 15*np.ones((n_steps))

    def calculate(self):
        for i in arange(n_steps-1):
            dvdt = 0.04*v[i]**2+5*v[i]+140-u[i]+I_in[i]
            dudt =a*(b*v[i]-u[i])
            
            if v[i]>=30:
                v[i+1]=c
                u[i+1]=u[i]+d
            else:
                v[i+1] = v[i]+dt*dvdt
                u[i+1] = u[i]+dt*dudt

    def plot_potential(self):
        t = np.linspace(0,n_steps/dt,n_steps)
        fig, ax1 = subplots()

        ax2 = ax1.twinx()
        ax1.plot(t, I_in, 'g-')
        ax2.plot(t, v, 'b-')

        ax1.set_xlabel('Time [s]')
        ax1.set_ylabel('Input Current', color='g') 
        ax2.set_ylabel('Membrane Potential (mV0', color='b')
        ax2.set_ylim([-85, 60])
        title("Response of Membrane Potential")
        show()


