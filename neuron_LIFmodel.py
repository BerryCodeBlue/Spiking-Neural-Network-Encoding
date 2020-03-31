import parameters as para
import numpy as np


class neuron_LIF_model:
    def __init__(self, input_signal, membrane_C, leak_R):
        self.V_thr = para.V_thr
        self.V_rest = para.V_rest
        self.V_spike = para.V_spike
        self. membrane_C = membrane_C
        self.leak_R = leak_R

        self.T = para.T
        self.dt = para.dt
        self.t_refr = para.refrac_duration_amount
        self.input_signal = input_signal
        self.time = np.arange(0, self.T + self.dt, self.dt)
        self.Vn = np.zeros(len(self.time))
        self.spike = np.zeros(len(self.time))

        self.Belta_Wave = True
        self.Vn[0] = 0
        self.neuron_response()

    def neuron_response(self):
        self.Vn[0] = self.V_rest
        i = 0
        while i < para.frame_amount - self.t_refr:
            print('starting...')
            # if (self.Vn[i] < self.V_thr):
            if (self.Vn[i] < self.V_thr) and (self.Vn[i] >= self.V_rest):
                self.Vn[i+1] = self.Vn[i] + self.dt/self.membrane_C * (-self.leak_R * (self.Vn[i] - self.V_rest) + self.input_signal[i])
                print('condition 1')
                self.spike[i] = 0
                i = i + 1
            elif (self.Vn[i] > self.V_thr) and (self.Vn[i] < self.V_spike):
                print('condition 2')
                self.Vn[i+1] = self.V_spike 
                self.spike[i] = 1
                self.Vn[i+2: i+1 + self.t_refr] = self.V_rest
                i = i + self.t_refr
            else:
                print('condition 3')
                self.Vn[i+1] = self.V_rest
                self.spike[i] = 0
                i = i + 1

        return self.spike, self.Vn





