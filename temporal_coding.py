import numpy as np
from Place_Field.neuron_LIFmodel import neuron_LIF_model
import parameters as para




def population_coding(input_signal):
    output1_sum = []
    output2_sum = []
    output3_sum = []

    for i in range(len(input_signal)):

        output1 = neuron_LIF_model(input_signal[i], para.membrane_C1, para.leak_R1)
        output1_sum.append(output1)
        output2 = neuron_LIF_model(input_signal[i], para.membrane_C2, para.leak_R2)
        output2_sum.append(output2)
        output3 = neuron_LIF_model(input_signal[i], para.membrane_C3, para.leak_R3)
        output3_sum.append(output3)

    return output1_sum, output2_sum, output3_sum
