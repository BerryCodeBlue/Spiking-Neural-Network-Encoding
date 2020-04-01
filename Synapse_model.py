import numpy as np


# TODO input signal should be neuron amount * time; In this case, the pre_neuron is delta_x, and the post neuron is errorx, of course after the time, the error should be inhibitated.

class Synapses():
    def __init__(self, pre_neuron, post_neuron):
        # self.neuron_rate_amount = 1
        # self.neuron_type_amount = len(post_neuron)  # input_signal: 6 * 2000
        # self.neuron_population = self.neuron_type_amount * self.neuron_rate_amount
        #
        # # self.total_synapses_amount = self.neuron_population * (self.neuron_population - 1)


        # # weights initializatio
        self.stability_factor = 2
        self.pre_neuron = pre_neuron
        self.post_neuron = post_neuron
        self.learning_rate = 0.7
        self.learning_rule()

    def learning_rule(self):

        pre_idx = np.nonzero(self.pre_neuron)
        post_idx = np.nonzero(self.post_neuron)
        self.w_sum = []
        self.time_window = 40
        self.loc_sum = []
        self.w_window_sumP = []
        self.weight_vector_sum = []


        for i in pre_idx[0]:
            for j in post_idx[0]:
                if j >i - self.time_window/2 and j <= i:
                    w_LTP = self.learning_rate * np.exp((j-i) + self.stability_factor)
                    self.w_window_sumP.append(w_LTP)
                    self.loc_sum.append(i)

                    weights_vector = [i, w_LTP]
                    self.weight_vector_sum.append(weights_vector)

                    #print("LTP")
                    #print(w_window_sumP)
                elif i < j and j< i + self.time_window/2:
                    w_LTD = - self.learning_rate * np.exp(-(j-i) + self.stability_factor)
                    #print("LTD")
                else:
                    pass

        return self.loc_sum, self.w_window_sumP, self.weight_vector_sum

            # dw = self.w - self.w_init[time]
            #
            # LTP_weight = np.exp(-dw)
            # LTP_t = np.exp(self.input_signal[conn_idx]) - self.stability_factor
            # LTP = LTP_weight * LTP_t
            #
            # LTD_weight = -np.exp(dw)
            # LTD_t = np.exp(1 - self.input_signal[conn_idx]) - self.stability_factor
            # LTD = LTD_weight * LTD_t
            #
            # self.w += self.learning_rate * (LTP + LTD).mean(0)
            # self.w_stor[conn_idx, conn_idx2] = self.w
