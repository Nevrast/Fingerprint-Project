import numpy as np
import matplotlib.pyplot as plt

def spectral_flatness(magnitudes):
    """
    :param magnitudes: array, complex values of each freqnecy bin
    :returns: sc_left - array, spectral flatness of left channel for each window
              sc_right - array, spectral flatness of right channel for each window
                         if file is mono returns -1
    """
    # puste macierze na parametry dla kazdego okna
    sf_left = np.array([])
    sf_right = np.array([])

    # obsluga plików mono
    if len(magnitudes.shape) == 2:
        # długość okna
        N = magnitudes.shape[0]

        # iteracja po okienkach
        for window in magnitudes.T:
            # algorytm spectral flatness, czyli średnia geometryczna podzielić na średnia arytmetyczna
            flatness = np.exp(np.sum(np.log(np.abs(window))) / N) / \
                       (np.sum(np.abs(window)) / N)
            # przypisanie do macierzy zwrotnej
            sf_left = np.append(sf_left, flatness)
        # dla plików mono kanał prawy zwraca "-1"
        sf_right = -1

    # obsługa plików dwukanałowych
    elif len(magnitudes.shape) == 3:
        N = magnitudes.shape[1]

        for window in magnitudes[0].T:
            flatness = np.exp(np.sum(np.log(np.abs(window))) / N) / \
                       (np.sum(np.abs(window)) / N)
            sf_left = np.append(sf_left, flatness)

        for window in magnitudes[1].T:
            flatness = np.exp(np.sum(np.log(np.abs(window))) / N) / \
                       (np.sum(np.abs(window)) / N)
            sf_right = np.append(sf_right, flatness)

    # jeśli coś nie zgadza się z rozimiarem macierzy wejściowej to robimy error, oczywiście nie przewiduje to wszystkich
    # przypadków, na przykład gdy :magnitudes: ma odpowiedni "kształt" ale złe wartości
    else:
        raise ValueError("Input is not supported")

    return sf_left, sf_right


def spectral_flatness_debug(sf_left, sf_right, time_bin, duration, sampling_rate, data):

    time = np.linspace(0, duration, duration * sampling_rate)

    fig = plt.figure(2)
    fig.canvas.set_window_title('Spectral Flatness')

    if type(sf_right) != type(sf_left):
        plot, plot_mono = plt.subplots()
        plot_mono.plot(time, data.flat, color='#c6c6c6', linewidth=0.4, label="Signal")
        plot_mono.plot(time_bin, sf_left, color='#23108f', linewidth=0.8, label="Spectral Centroid")
        plot_mono.set_xlabel('Time [s]')
        plot_mono.set_ylabel('Spectral flatness, normalized amplitudes')
        plot_mono.minorticks_on()
        plot_mono.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_mono.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_mono.legend(loc='lower left', bbox_to_anchor=(0., 1.))

    else:
        plot_l = plt.subplot2grid((2, 2), (0, 0))
        plot_r = plt.subplot2grid((2, 2), (0, 1))
        plot_both = plt.subplot2grid((2, 2), (1, 0), colspan=2)

        plot_l.plot(time_bin, sf_left, color='#23108f', linewidth=0.8, label='Spectral Flatness')
        plot_l.set_title('Left channel')
        plot_l.set_xlabel('Time [s]')
        plot_l.set_ylabel('Spectral Flatness')
        plot_l.minorticks_on()
        plot_l.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_l.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_signal_l = plot_l.twinx()
        plot_signal_l.plot(time, data[0].flat, color='#c6c6c6', linewidth=0.4, label="Signal")
        plot_signal_l.set_ylabel('Normalized amplitude')
        plot_l.set_zorder(plot_signal_l.get_zorder() + 1)
        plot_l.patch.set_visible(False)
        plot_l.legend(loc='lower left', bbox_to_anchor=(0., 1.))
        plot_signal_l.legend(loc='lower right', bbox_to_anchor=(1., 1.))

        plot_r.plot(time_bin, sf_right, color='r', linewidth=0.8, label='Spectral Flatness')
        plot_r.set_title('Right channel')
        plot_r.set_xlabel('Time [s]')
        plot_r.set_ylabel('Spectral Flatness')
        plot_r.minorticks_on()
        plot_r.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_r.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.4)
        plot_signal_r = plot_r.twinx()
        plot_signal_r.plot(time, data[1].flat, color='#c6c6c6', linewidth=0.4, label='Signal')
        plot_signal_r.set_ylabel('Normalized amplitude')
        plot_r.set_zorder(plot_signal_r.get_zorder() + 1)
        plot_r.patch.set_visible(False)
        plot_r.legend(loc='lower left', bbox_to_anchor=(0., 1.))
        plot_signal_r.legend(loc='lower right', bbox_to_anchor=(1., 1.))

        plot_both.plot(time_bin, sf_left, color='#23108f', linewidth=0.8, zorder=10, label='Left')
        plot_both.plot(time_bin, sf_right, color='#de0000', linewidth=0.8, zorder=11, label='Right')
        plot_both.set_title('Both channels')
        plot_both.set_xlabel('Time [s]')
        plot_both.set_ylabel('Spectral Flatness')
        plot_both.minorticks_on()
        plot_both.grid(b=True, which='major', color='#93a1a1', alpha=0.5, linestyle='-')
        plot_both.grid(b=True, which='minor', color='#93a1a1', linestyle='--', alpha=0.2)
        plot_both.legend(loc='upper left')

        plt.subplots_adjust(wspace=0.25)
    plt.suptitle('Spectral Flatness', fontsize=16)

