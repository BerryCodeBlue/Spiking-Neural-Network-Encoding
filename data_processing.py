import numpy as np


def normalization(datainput):
    max_collec = []
    min_collec = []
    for i in range(len(datainput)):
        l = datainput[i]
        data_max = max(l)
        data_min = min(l)
        max_collec.append(data_max)
        min_collec.append(data_min)

    data_max = float(max(max_collec))
    data_min = float(min(min_collec))

    range_min = 0
    range_max = 1

    l = np.array(datainput)
    l_float = l.astype(np.float)

    scale_ratio = (range_max - range_min) / (data_max - data_min)
    output = scale_ratio * (l_float - data_min) + range_min

    return output

def scal_mapping(datainput):
    scale_factor_x = 50
    scale_factor_y = 50
    scale_factor_z = 30

    nor_x_domi = (max(datainput[0]) - min(datainput[0])) / scale_factor_x
    nor_y_domi = (max(datainput[1]) - min(datainput[1])) / scale_factor_y
    nor_z_domi = (max(datainput[2]) - min(datainput[2])) / scale_factor_z

    return nor_x_domi, nor_y_domi, nor_z_domi

def Place_field_processing(input_pre, place_field_input, place_cell_matrix):
    x_pre = input_pre[0]
    y_pre = input_pre[1]
    z_pre = input_pre[2]
    delta_x = place_field_input[0] - x_pre
    delta_y = place_field_input[1] - y_pre
    delta_z = place_field_input[2] - z_pre
    input_matrix = [delta_x, delta_y, delta_z]
    error_matrix = np.array(input_matrix).dot(np.array(place_cell_matrix))

    return error_matrix


def read_data_files():
    f = open("input_signal.txt", "r")
    lines = f.readlines()
    delta_x_r = []
    delta_y_r = []
    delta_z_r = []

    err_step_x_r = []
    err_step_y_r = []
    err_step_z_r = []

    for x in lines:
        delta_x_r.append(x.split(' ')[0])
        delta_y_r.append(x.split(' ')[1])
        delta_z_r.append(x.split(' ')[2])
        err_step_x_r.append(x.split(' ')[3])
        err_step_y_r.append(x.split(' ')[4])
        err_step_z_r.append(x.split(' ')[5])
    f.close()

    return delta_x_r, delta_y_r, delta_z_r, err_step_x_r, err_step_y_r, err_step_z_r

def read_data_files_vertical():
    f = open("input_signal.txt", "r")
    lines = f.readlines()



def read_file(filename):
    f = open(filename, "r")
    lines = f.readlines()
    delta_x_spike = []
    delta_y_spike = []
    delta_z_spike = []

    for x in lines:
        delta_x_spike.append(x.split(' ')[0])
        delta_y_spike.append(x.split(' ')[1])
        delta_z_spike.append(x.split(' ')[2])

    f.close()

    delta_x_spike = np.array(delta_x_spike).astype(float)
    delta_y_spike = np.array(delta_y_spike).astype(float)
    delta_z_spike = np.array(delta_z_spike).astype(float)

    output = [delta_x_spike, delta_y_spike, delta_z_spike]

    return output

def read_groundtruth_file(filename):
    f = open(filename, "r")
    lines = f.readlines()
    delta_x_spike = []
    delta_y_spike = []
    delta_z_spike = []

    for x in lines:
        delta_x_spike.append(x.split(' ')[3])
        delta_y_spike.append(x.split(' ')[7])
        delta_z_spike.append(x.split(' ')[11])

    f.close()

    delta_x_spike = np.array(delta_x_spike).astype(float)
    delta_y_spike = np.array(delta_y_spike).astype(float)
    delta_z_spike = np.array(delta_z_spike).astype(float)

    output = [delta_x_spike, delta_y_spike, delta_z_spike]

    return output


def find_the_valid_idx(input):
    sum = []

    for i in input:
        if len(i) == 0:
            pass
        else:
            sum = sum + i
    return sum
