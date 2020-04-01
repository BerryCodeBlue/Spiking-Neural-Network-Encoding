import numpy as np
from neuron_LIFmodel import neuron_LIF_model
from matplotlib import pyplot as plt
import parameters as para
from data_processing import normalization
from temporal_coding import population_coding
#from Create_plots.create_plots import plot_spiketrains
#from Visual_Processing.synapse_output import SynapseLearning


class RateCoding:

    def __init__(self):

        self.valid_x_sum = []
        self.valid_y_sum = []
        self.valid_z_sum = []
        self.rate_coding()
        #self.significant_error_events()
        #self.synapse_para = SynapseLearning()

    def rate_coding(self):
        print("start")
        self.delta_x_r, self.delta_y_r, self.delta_z_r = self.read_input_file('input_draw_coord.txt')

        ## Uncomment the following line to encode the groundtruth data
        # self.delta_x_r, self.delta_y_r, self.delta_z_r = self.read_spike_file('input_true_coord.txt')

        data_in_total = [self.delta_x_r, self.delta_y_r, self.delta_z_r]
        data_in_total_nor = normalization(data_in_total)
        input_data_in_total = np.multiply(np.array(data_in_total_nor, dtype=float), 20e-4)
        self.neuron_output1, self.neuron_output2, self.neuron_output3 = population_coding(input_data_in_total)
        return self.neuron_output1, self.neuron_output2, self.neuron_output3   #6*3

    def read_input_file(self, filename):
        f = open(filename, "r")  #f = open("input_spikes_oh_test.txt", "r")
        lines = f.readlines()
        delta_x_r = []
        delta_y_r = []
        delta_z_r = []

        for x in lines:
            delta_x_r.append(x.split(' ')[0])
            delta_y_r.append(x.split(' ')[1])
            delta_z_r.append(x.split(' ')[2])
        f.close()
        return delta_x_r, delta_y_r, delta_z_r


    def significant_movement(self):

        idx = self.synapse_para.xloc_sum
        idy = self.synapse_para.yloc_sum
        idz = self.synapse_para.zloc_sum

        for i in idx:
            valid_x = self.delta_x_r[i]
            self.valid_x_sum.append(valid_x)

        for i in idy:
            valid_y = self.delta_y_r[i]
            self.valid_y_sum.append(valid_y)

        for i in idz:
            valid_z = self.delta_z_r[i]
            self.valid_z_sum.append(valid_z)

        return self.valid_x_sum, self.valid_y_sum, self.valid_z_sum


    def significant_error_events(self):

        self.wx = self.synapse_para.wx_window_sum
        self.wy = self.synapse_para.wy_window_sum
        self.wz = self.synapse_para.wz_window_sum

        self.wx_vector = self.synapse_para.weight_vector_x
        self.wy_vector = self.synapse_para.weight_vector_y
        self.wz_vector = self.synapse_para.weight_vector_z

        # plot_learning_weights(wx_vector)
        # plt.show()
        #
        # plot_learning_weights(wy_vector)
        # plt.show()
        #
        # plot_learning_weights(wz_vector)
        # plt.show()

        return self.wx_vector, self.wy_vector, self.wz_vector, self.wx, self.wy, self.wz

    def start_input_coding(self):
        population = RateCoding()
        neuron_1 = population.neuron_output1
        neuron_2 = population.neuron_output2
        neuron_3 = population.neuron_output3

        # Plot the Spiketrains

        NeuralData = [neuron_1[0].spike, neuron_1[1].spike, neuron_1[2].spike,
                      neuron_2[0].spike, neuron_2[1].spike, neuron_2[2].spike,
                      neuron_3[0].spike, neuron_3[1].spike, neuron_3[2].spike,]

        # merge the sequences
        delta_x_population_sum = np.zeros(2000)
        delta_y_population_sum = np.zeros(2000)
        delta_z_population_sum = np.zeros(2000)

        for i in range(2000):
            if neuron_1[0].spike[i] or neuron_2[0].spike[i] or neuron_3[0].spike[i] != 0:
                delta_x_population_sum[i] = 1
            if neuron_1[1].spike[i] or neuron_2[1].spike[i] or neuron_3[1].spike[i] != 0:
                delta_y_population_sum[i] = 1
            if neuron_1[2].spike[i] or neuron_2[2].spike[i] or neuron_3[2].spike[i] != 0:
                delta_z_population_sum[i] = 1

        return delta_x_population_sum, delta_y_population_sum, delta_z_population_sum

#========================Run================================================
test1 = RateCoding()
delta_x_population_sum, delta_y_population_sum, delta_z_population_sum = test1.start_input_coding()
NeuralData_sum = delta_x_population_sum, delta_y_population_sum, delta_z_population_sum

fig = plt.gcf()
fig.set_size_inches(30,3)
#fig.savefig("spiketrains_draw.png")
#np.savetxt('input_spikes_draw.txt', np.c_[delta_x_population_sum, delta_y_population_sum, delta_z_population_sum])


## Uncomment the following line to encode the groundtruth data
fig.savefig("spiketrains_true.png")
np.savetxt('input_spikes_true.txt', np.c_[delta_x_population_sum, delta_y_population_sum, delta_z_population_sum])
plt.show()