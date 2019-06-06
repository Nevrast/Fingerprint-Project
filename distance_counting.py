import numpy as np
from scipy.spatial import minkowski_distance
from copy import copy
import matplotlib.pyplot as plt


def diff_counting(ref_fing_l, ref_fing_r, test_fing_l, test_fing_r):
    temp_ref_fing_l = copy(ref_fing_l)
    temp_ref_fing_r = copy(ref_fing_r)
    temp_test_fing_l = copy(test_fing_l)
    temp_test_fing_r = copy(test_fing_r)
    # check if files have same duration or sampling frequency
    if temp_ref_fing_l.shape != temp_test_fing_l.shape:
        print('Files must have same duration and/or sampling frequency.')
        dst_l, average_dst_l, dst_r, average_dst_r = None, None, None, None
        return dst_l, average_dst_l, dst_r, average_dst_r
    # normalizacja parametrów w fprincie
    for i in range(len(temp_ref_fing_l)):
        max_ref_l = np.max(temp_ref_fing_l[i])
        temp_ref_fing_l[i] = temp_ref_fing_l[i] / np.max(temp_ref_fing_l[i])
        temp_test_fing_l[i] = temp_test_fing_l[i] / max_ref_l
    # print(ref_fing_l, test_fing_l)
    dst_l = minkowski_distance(temp_ref_fing_l.T, temp_test_fing_l.T)
    average_dst_l = np.average(dst_l)

    if type(temp_ref_fing_r[0]) == np.ndarray:
        for i in range(len(temp_ref_fing_r)):
            max_ref_r = np.max(temp_ref_fing_r[i])
            temp_ref_fing_r[i] = temp_ref_fing_r[i] / np.max(temp_ref_fing_r[i])
            temp_test_fing_r[i] = temp_test_fing_r[i] / max_ref_r
        # obliczanie dystansu miedzy macierzami wg. metryki euclidesowej
        dst_r = minkowski_distance(temp_ref_fing_r.T, temp_test_fing_r.T)
        average_dst_r = np.average(dst_r)
    else:
        dst_r = None
        average_dst_r = None

    # słownik na parametry
    dst_dict = {
        'zc_dst_l': distance(temp_ref_fing_l[0], temp_test_fing_l[0]),
        'sc_dst_l': distance(temp_ref_fing_l[1], temp_test_fing_l[1]),
        'sf_dst_l': distance(temp_ref_fing_l[2], temp_test_fing_l[2]),
        'rms_dst_l': distance(temp_ref_fing_l[3], temp_test_fing_l[3]),
        'ro_dst_l': distance(temp_ref_fing_l[4], temp_test_fing_l[4]),
        'psd_dst_l': distance(temp_ref_fing_l[5], temp_test_fing_l[5]),
        'zc_dst_r': distance(temp_ref_fing_r[0], temp_test_fing_r[0]),
        'sc_dst_r': distance(temp_ref_fing_r[1], temp_test_fing_r[1]),
        'sf_dst_r': distance(temp_ref_fing_r[2], temp_test_fing_r[2]),
        'rms_dst_r': distance(temp_ref_fing_r[3], temp_test_fing_r[3]),
        'ro_dst_r': distance(temp_ref_fing_r[4], temp_test_fing_r[4]),
        'psd_dst_r': distance(temp_ref_fing_r[5], temp_test_fing_r[5])
    }

    return dst_l, average_dst_l, dst_r, average_dst_r, dst_dict


def distance(x, y):
    dst = np.sqrt(np.power(y - x, 2))
    return dst


def distance_plots(dst_l, dst_r, dst_dic, time):
    if dst_r is not None:
        plot_l_apart = plt.subplot2grid((2, 2), (0, 0))
        plot_r_apart = plt.subplot2grid((2, 2), (0, 1))
        plot_all = plt.subplot2grid((2, 2), (1, 0), colspan=2)

        plot_l_apart.set_title('Left channel distances')
        plot_l_apart.plot(time, dst_dic['zc_dst_l'], label='Zero Crossing', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['sc_dst_l'], label='Spectral Centroid', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['sf_dst_l'], label='Spectral Flatness', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['rms_dst_l'], label='Root Mean Square', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['ro_dst_l'], label='Spectral Rolloff', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['psd_dst_l'], label='Average PSD', linewidth=0.6)
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
        plot_r_apart.plot(time, dst_dic['psd_dst_r'], label='Average PSD', linewidth=0.6)
        plot_r_apart.minorticks_on()
        plot_r_apart.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_r_apart.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
        plot_r_apart.legend(loc='lower right', bbox_to_anchor=(1., 1.), mode='expand')

        plot_all.set_title('Fingerprint distances')
        plot_all.plot(time, dst_l, label='Left Channel', linewidth=0.6)
        plot_all.plot(time, dst_r, label='Right Channel', linewidth=0.6)
        plot_all.minorticks_on()
        plot_all.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_all.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
        plot_all.legend(loc='upper left')

    else:
        plot_l_apart = plt.subplot2grid((2, 2), (0, 0), colspan=2)
        plot_all = plt.subplot2grid((2, 2), (1, 0), colspan=2)

        plot_l_apart.set_title('Left channel distances')
        plot_l_apart.plot(time, dst_dic['zc_dst_l'], label='Zero Crossing', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['sc_dst_l'], label='Spectral Centroid', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['sf_dst_l'], label='Spectral Flatness', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['rms_dst_l'], label='Root Mean Square', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['ro_dst_l'], label='Spectral Rolloff', linewidth=0.6)
        plot_l_apart.plot(time, dst_dic['psd_dst_l'], label='Average PSD', linewidth=0.6)
        plot_l_apart.minorticks_on()
        plot_l_apart.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_l_apart.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
        plot_l_apart.legend(loc='lower left', bbox_to_anchor=(0., 1.), ncol=2)

        plot_all.set_title('Fingerprint distances')
        plot_all.plot(time, dst_l, label='Left Channel', linewidth=0.6)
        plot_all.minorticks_on()
        plot_all.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_all.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
        plot_all.legend(loc='upper left')

    plt.show()
