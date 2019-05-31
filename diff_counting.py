import argparse
from scipy.spatial import minkowski_distance
from fingerprint_creating import fing_creat
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="This is a script which provides information about quality"
                                             " degradation level in chosen signal. User indicates the reference signal"
                                             " (first argument) and the measured signal (second argument).")

parser.add_argument("reference", help="- reference signal")
parser.add_argument("input", help="- input signal")
parser.add_argument("-o", "--output", help="- output file")
parser.add_argument("-d", "--debug", help="- debugging mode, this argument is called without any value", default=False,
                    action='store_true')

args = parser.parse_args()

REFERENCE_PATH = args.reference
INPUT_PATH = args.input
if args.output:
    OUTPUT_PATH = args.output

if args.debug:
    print("Input file: ", INPUT_PATH)
    print("Reference file: ", REFERENCE_PATH)
    if args.output:
        print("Reference file: ", OUTPUT_PATH)


def diff_counting(ref, input):
    ref_fing_l, ref_fing_r, ref_time = fing_creat(ref)
    input_fing_l, input_fing_r, input_time = fing_creat(input)

    if ref_fing_r.shape != input_fing_r.shape:
        missing_zeros = ref_fing_l.shape[1] - input_fing_l.shape[1]
        zeros = np.zeros((5, missing_zeros))
        input_fing_l = np.append(input_fing_l, zeros, axis=-1)
        input_fing_r = np.append(input_fing_r, zeros, axis=-1)

    for i in range(len(ref_fing_l)):
        max_ref_l = np.max(ref_fing_l[i])
        max_ref_r = np.max(ref_fing_r[i])
        ref_fing_l[i] = ref_fing_l[i] / np.max(ref_fing_l[i])
        ref_fing_r[i] = ref_fing_r[i] / np.max(ref_fing_r[i])
        input_fing_l[i] = input_fing_l[i] / max_ref_l
        input_fing_r[i] = input_fing_r[i] / max_ref_r

    dst_l = minkowski_distance(ref_fing_l.T, input_fing_l.T)
    dst_r = minkowski_distance(ref_fing_r.T, input_fing_r.T)
    dst_dic = {
        'zc_dst_l': distance(ref_fing_l[0], input_fing_l[0]),
        'sc_dst_l': distance(ref_fing_l[1], input_fing_l[1]),
        'sf_dst_l': distance(ref_fing_l[2], input_fing_l[2]),
        'rms_dst_l': distance(ref_fing_l[3], input_fing_l[3]),
        'ro_dst_l': distance(ref_fing_l[4], input_fing_l[4]),
        'zc_dst_r': distance(ref_fing_r[0], input_fing_r[0]),
        'sc_dst_r': distance(ref_fing_r[1], input_fing_r[1]),
        'sf_dst_r': distance(ref_fing_r[2], input_fing_r[2]),
        'rms_dst_r': distance(ref_fing_r[3], input_fing_r[3]),
        'ro_dst_r': distance(ref_fing_r[4], input_fing_r[4])
    }

    init_plots(dst_l, dst_r, dst_dic, ref_time)


def distance(x, y):
    dst = np.array([])
    for i in range(len(x)):
        dst = np.append(dst, np.sqrt(np.power(y[i]-x[i], 2)))

    return dst


def init_plots(dst, dst2, dst_dic, time):
    plot_l_apart = plt.subplot2grid((2, 2), (0, 0))
    plot_r_apart = plt.subplot2grid((2, 2), (0, 1))
    plot_all = plt.subplot2grid((2, 2), (1, 0), colspan=2)

    plot_l_apart.set_title('Left channel distances')
    plot_l_apart.plot(time, dst_dic['zc_dst_l'], label='Zero Crossing', linewidth=0.6)
    plot_l_apart.plot(time, dst_dic['sc_dst_l'], label='Spectral Centroid', linewidth=0.6)
    plot_l_apart.plot(time, dst_dic['sf_dst_l'], label='Spectral Flatness', linewidth=0.6)
    plot_l_apart.plot(time, dst_dic['rms_dst_l'], label='Root Mean Square', linewidth=0.6)
    plot_l_apart.plot(time, dst_dic['ro_dst_l'], label='Spectral Rolloff', linewidth=0.6)
    plot_l_apart.minorticks_on()
    plot_l_apart.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
    plot_l_apart.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
    plot_l_apart.legend(loc='lower left', bbox_to_anchor=(0., 1.), ncol=2)

    plot_r_apart.set_title('Right channel distances')
    plot_r_apart.plot(time, dst_dic['zc_dst_r'], label='Zero Crossing', linewidth=0.6)
    plot_r_apart.plot(time, dst_dic['sc_dst_r'], label='Spectral Centroid', linewidth=0.6)
    plot_r_apart.plot(time, dst_dic['sf_dst_r'], label='Spectral Flatness', linewidth=0.6)
    plot_r_apart.plot(time, dst_dic['rms_dst_r'], label='Root Mean Square', linewidth=0.6)
    plot_r_apart.plot(time, dst_dic['ro_dst_r'], label='Spectral Rolloff', linewidth=0.6)
    plot_r_apart.minorticks_on()
    plot_r_apart.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
    plot_r_apart.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
    plot_r_apart.legend(loc='lower right', bbox_to_anchor=(1., 1.), mode='expand')

    plot_all.set_title('Fingerprint distances')
    plot_all.plot(time, dst, label='Left Channel', linewidth=0.6)
    plot_all.plot(time, dst2, label='Right Channel', linewidth=0.6)
    plot_all.minorticks_on()
    plot_all.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
    plot_all.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
    plot_all.legend(loc='upper left')

    plt.show()

#wywołanie funkcji
diff_counting(REFERENCE_PATH, INPUT_PATH)


