import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import read, write
from scipy import signal
import sounddevice as sd

starting_filename = "piano2.wav"


class AudioProcessing(object):
    __slots__ = ('original_audio_data', 'transformed_audio_data', 'sample_freq')

    def __init__(self):
        self.load_file(starting_filename)

    def load_file(self, input_audio_path):
        self.sample_freq, self.original_audio_data = read(input_audio_path)
        self.original_audio_data = self.convert_to_mono_audio(self.original_audio_data)
        self.transformed_audio_data = self.original_audio_data
        # self.add_delay(0)

    def convert_to_mono_audio(self, input_audio):
        output_audio = []
        if len(input_audio.shape) > 1:
            for e in input_audio:
                output_audio.append((e[0] / 2) + (e[1] / 2))
        else:
            output_audio = input_audio

        return np.array(output_audio, dtype='int16')

    def add_delay(self, delay):
        self.resetData()
        output_delay = delay * self.sample_freq
        output_audio = np.zeros(len(self.transformed_audio_data) + int(output_delay), dtype='int64')

        for count, e in enumerate(self.transformed_audio_data):
            output_audio[count] += e
            output_audio[count + int(output_delay)] += e

        self.transformed_audio_data = output_audio.astype(np.int16)

    def add_reverb(self, pre_delay, decay, interval):
        self.resetData()
        temp_data = self.transformed_audio_data
        output_delay = (pre_delay + decay) * self.sample_freq
        pre_delay *= self.sample_freq
        reflection_delay = interval * self.sample_freq + 1
        output_audio = np.zeros(len(temp_data) + int(output_delay), dtype='float64')
        n_reflections = int(decay / interval)
        # expotential_decrease = np.exp(np.linspace(np.e, 1, n_reflections + 2))[1:-1]
        linear_decrease = np.linspace(0, 1, n_reflections + 2)[::-1]
        linear_decrease = linear_decrease[1:-1]

        for i, sample in enumerate(temp_data):
            output_audio[i] += sample
            for j, reflection in enumerate(linear_decrease):
                output_audio[i + int(pre_delay) + int(reflection_delay * j)] += sample * reflection

        self.transformed_audio_data = output_audio.astype(np.int16)

    def add_flanger(self, frequency, amplitude, type):
        self.resetData()
        length = len(self.transformed_audio_data)
        y = np.zeros(length, dtype='int64')
        x = self.original_audio_data
        amplitude *= self.sample_freq

        if type == "sine":
            for i in range(length - int(2 * amplitude)):
                y[i] = x[i] + x[int(i + amplitude + round(amplitude * np.sin(2 * np.pi * i * frequency/self.sample_freq)))]
        else:
            for i in range(length - int(2 * amplitude)):
                y[i] = x[i] + x[int(i + amplitude + round(amplitude * signal.sawtooth(2 * np.pi * i * frequency / self.sample_freq, 0.5)))]
        '''
        if type == "triangle":
            flanger = 1 + signal.sawtooth(2 * np.pi * frequency * n_samples, 0.5)

        elif type == "sine":
            flanger = 1 + np.sin(2 * np.pi * frequency * n_samples)

        else:
            exit(1)

        print(flanger)
        index = np.around(n_samples - self.sample_freq * amplitude * flanger)
        index[index < 0] = 0
        index[index > (length - 1)] = length - 1

        # index = np.around(n_samples-Fs*)
        temp_data = self.original_audio_data

        for i in range(length):
            output_audio[i] = np.float(temp_data[i]) + np.float(temp_data[int(index[i])])

        self.transformed_audio_data = output_audio.astype(np.int16)
        '''
        self.transformed_audio_data = y.astype(np.int16)

    def play(self):
        sd.play(self.transformed_audio_data, self.sample_freq)

    def stop(self):
        sd.stop()

    def resetData(self):
        self.transformed_audio_data = self.original_audio_data
