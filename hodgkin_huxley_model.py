# Hodgkin-Huxley model
import numpy as np
from pylab import *

class neuron_HH_model:
    def __init__(self):
        self.dt = 0.01
        self.n_steps = 10000
        self.E_Na = +55 
        self.E_K = -75
        self.E_L = -69

        self.g_Na = 120
        self.g_K  = 36
        self.g_L  = 0.3

        self.C = 0.5

        self.m = np.zeros((n_steps,))
        self.n = np.zeros((n_steps,))
        self.h = np.zeros((n_steps,))

        self.u = np.ones((n_steps,))
                    
        self.ampl = 10
        self.I_in = ampl*np.ones((n_steps,))
                    
        self.u[0] = -65
        self.m[0] = 0.05
        self.n[0] = 0.31
        self.h[0] = 0.6

    def calculate(self):

        alpha_n = lambda u: (0.1-0.01*(u+65))/(exp(1-0.1*(u+65))-1)
        beta_n  = lambda u: 0.125*exp(-(u)/80)
        alpha_m = lambda u: (2.5-0.1*(u+65))/(exp(2.5-0.1*(u+65))-1)
        beta_m  = lambda u: 4*exp(-(u+65)/18)
        alpha_h = lambda u: 0.07*exp(-(u+65)/20)
        beta_h  = lambda u: 1/(exp(3.0-0.1*(u+65))+1)


        for i in arange(n_steps-1):
            
            n[i+1] = n[i] + dt*(alpha_n(u[i]) * (1-n[i])-beta_n(u[i])*n[i])
            m[i+1] = m[i] + dt*(alpha_m(u[i]) * (1-m[i])-beta_m(u[i])*m[i])
            h[i+1] = h[i] + dt*(alpha_h(u[i]) * (1-h[i])-beta_h(u[i])*h[i])
            
            I_k_sum = g_Na*m[i]**3*h[i]*(u[i]-E_Na) + g_K*n[i]**4*(u[i]-E_K)+g_L*(u[i]-E_L)
            u[i+1]  = u[i]+dt*(I_in[i]-I_k_sum)/C


    def plot_potential(self):
        tt = np.linspace(0, n_steps/dt, n_steps)
        fig, ax1 = subplots()

        ax2 = ax1.twinx()
        ax1.plot(tt, I_in, 'g-')
        ax2.plot(tt, u, 'b-')

        ax1.set_xlabel('Time [s]')
        ax1.set_ylabel('Input Current', color='g') # which unit?
        ax2.set_ylabel('Membrane Potential (mV)', color='b')
        ax2.set_ylim([-85, 60])
        title("Response of Membrane Potential")
        show()