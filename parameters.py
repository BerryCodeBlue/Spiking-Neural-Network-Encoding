##!/usr/bin/env python

import numpy as np

# Path settings
input_path = None
output_path = None

# Input image
frame_amount = 2000

# Neuronal Dynamics

# mV
V_thr = -20e-3
V_rest = -60e-3
V_spike = Vspike=20e-3

T = 25e-6 * frame_amount
dt = 25e-6   # step normall: 25e-6 with T = 0.05
refrac_duration_amount = 1

# Neuron 1
membrane_C1 = 1e-6  #   0.4e-6
leak_R1 = 50e-6    #  50e-6

# Neuron 2
membrane_C2 = 1e-6  #   0.4e-6
leak_R2 = 100e-6    #  50e-6

# Neuron 3
membrane_C3 = 1e-6  #   0.4e-6
leak_R3 = 200e-6    #  50e-6


