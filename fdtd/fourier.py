
# def pretty_freqs():
#     ["KHz", "MHz", "GHz", "THz"]
#     {:.2f}"\
#                 .format(fft_bin_resolution)

# In the electrical domain,

# https://inst.eecs.berkeley.edu/~ee232/sp17/discussions/Discussion%207%20-%20Photonic%20circuit%20simulation.pptx



class FrequencyRoutines:
    # originally called FrequencyDomain, renamed because 'fd' is already a namespace
    # give it an id or name of a detector or SoftArbitraryPointSource
    # or an arbitrary numpy list,
    # converts it into the frequency domain.
    # frequency in Hz, not angular frequency
    # checks the class type
    # pad to get frequency bins



    def __init__(grid, input_name=None, input_id=None):
        self.grid = grid


    # def S_parameters():
    # #

    def padding_and_timing(self, input_data, freq_window_tuple=None, fft_num_bins_in_window=None,
                                            fft_bin_freq_resolution=None, dt):
        '''
        input_data must be a 1d array with the time history of one detector. the length of input_data
        is expected to be the same as time_steps_passed.

        - fft_num_bins
        - FFT bin resolution (optional) Hz.
        '''
        # Paraphrasing from the great explanation from
        # https://www.bitweenie.com/listings/fft-zero-padding/
        # there are two different frequency resolutions at play.
        # The first one, a physical resolution,

        input_length = input_data.shape()[0]

        begin_freq, end_freq = begin_end_freq_tuple
        end_time = input_length * dt
        #
        # if(not fft_num_bins or fft_bin_resolution):
        #     print("One of fft_num_bins or fft_bin_resolution must be specified")

        if(fft_num_bins == None and not fft_bin_resolution == None):
            fft_num_bins_in_window = ((begin_freq-end_freq)/fft_bin_resolution)

        elif(not (fft_num_bins_in_window or fft_bin_resolution)):
            # the window is the default, whole array
            fft_num_bins_in_window = np.len(input_data)

        waveform_frequency_resolution = 1.0 / end_time
        fft_bin_resolution = (1.0 / dt) / (fft_num_bins_in_window)
        print("Waveform data has an intrinsic resolution of: {:.2f} Hz"\
                    .format(waveform_frequency_resolution))
        print("FFT bin: {:.2f} Hz"\
                    .format(fft_bin_resolution))

        required_length = ceil(fft_num_bins_in_window / ((end_freq-begin_freq) * dt))

        # There are some
        # the key is that indeed no extra information is being added;
        # sinc interplolation
        # https://dsp.stackexchange.com/questions/31783/mathematical-justification-for-zero-padding

        # https://dsp.stackexchange.com/questions/741/why-should-i-zero-pad-a-signal-before-taking-the-fourier-transform
        # https://dsp.stackexchange.com/questions/24410/zero-padding-of-fft/24426#24426

        # This seems like magic - how could this be?
        # there are other ways to get a higher bin resolution
        existing_times = bd.linspace(0,grid.time_passed, n=grid.time_steps_passed)
        padded_times = bd.linspace(0,grid.time_passed, n=required_padding)

        times = bd.concatenate(bd.linspace(0,grid.time_passed, n=grid.time_steps_passed)

        spectrum_freqs = bd.fftfreq(len(voltages), d=pcb.grid.time_step)

        begin_freq_idx = bd.abs(spectrum_freqs - begin_freq).argmin()
        end_freq_idx = bd.abs(spectrum_freqs - end_freq).argmin()



        return
        #test that end_time is time_passed

    #UNTESTED
    # def S_parameters(waveform, node):
    #     null_waveform = bd.zeros_like(waveform)
    #     for idx, n in node_objects:
    #         n.waveform = null_waveform
    #         # grid.run()
    #         # monitor
    #         grid.reset()

    def complex_impedance():
        pass

    def plot_impedance():
        '''
        Frequencies are in Hz.
        '''

        begin_freq, end_freq = begin_end_freq_tuple
        desired_binning_Npoints = 300 #100 points below F_max
        required_length = int(desired_binning_Npoints / ((begin_freq-end_freq) * grid.time_step))
        print(required_length)

        voltages = bd.pad(voltages, (0, required_length), 'edge')
        currents = bd.pad(currents, (0, required_length), 'edge')

        # assumes a uniform timestep. It might be useful to add a .times vector to the grid
        # if the timestep is made variable at some point.
        # on the other hand, doing a non-uniform FFT is probably non-trivial at this point anyway

        voltage_spectrum = bd.fft(voltages)
        current_spectrum = bd.fft(currents)




        plt.plot(times_padded, voltages)

        plt.plot(times_padded, currents)
        plt.plot(spectrum_freqs[begin_freq:end_freq], abs(voltage_spectrum[begin_freq:end_freq]), label="volt")
        plt.plot(spectrum_freqs[begin_freq:end_freq], abs(current_spectrum[begin_freq:end_freq]), label="curr")

        # power_spectrum = -1.0*((voltage_spectrum[begin_freq:end_freq]*np.conj(current_spectrum[begin_freq:end_freq])).real)
        # power_spectrum /= np.linalg.norm(power_spectrum)
        # plt.plot(spectrum_freqs[begin_freq:end_freq],power_spectrum)

        plt.figure()
        #
        # Z0 = scipy.constants.physical_constants['characteristic impedance of vacuum'][0]

        impedance_spectrum = abs(voltage_spectrum/current_spectrum)

        plt.plot(spectrum_freqs[begin_freq:end_freq],impedance_spectrum[begin_freq:end_freq])
        # plt.plot(spectrum_freqs[begin_freq:end_freq],impedance_spectrum[begin_freq:end_freq])
        plt.savefig('/tmp/impedance_spectrum.svg')
        # # plt.plot(spectrum_freqs,(voltage_spectrum/current_spectrum))
        # plt.plot(spectrum_freqs[begin_freq:end_freq],(voltage_spectrum[begin_freq:end_freq]/current_spectrum[begin_freq:end_freq]).real)
        # plt.plot(spectrum_freqs[begin_freq:end_freq],(voltage_spectrum[begin_freq:end_freq]/current_spectrum[begin_freq:end_freq]).imag)

        plt.draw()
        plt.pause(0.001)
        input()
        #
        # print("Z: ", impedance_spectrum[np.abs(spectrum_freqs - 2.3e9).argmin()])
        #
        # files = ['/tmp/voltages.svg', '/tmp/currents.svg', '/tmp/spectrum.svg', '/tmp/impedance_spectrum.svg', "U_patch_antenna_designer.py", "stdout.log"]
        # store.ask(files)