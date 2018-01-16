import librosa
import lyric_parser
import matplotlib.pyplot as plt
from numpy import linalg as LA
import numpy as np
import npp


def ms2sample(time_ms,sr=44100):

    time_sample = int(round(time_ms /1000 * sr, 0))

    return time_sample

def mute_start(sig):
    sig[0:1000] = 0
    return sig

time = lyric_parser.l.get_time_before_vocal()
time = ms2sample(time)


from scipy import signal
from numpy import diff,sign,sin,exp,linspace

# def filter(sig):
#     b, a = signal.ellip(4, 0.01, 120, 0.125, output='ba')
#     return signal.filtfilt(b, a, sig, method="gust")

time = time //2 -1000

# example data with some peaks:
# data = voc[time//2:time//2+300]
# data = np.convolve(np.zeros((50))+1/50,data,mode='same')

# pad = np.pad(mix[:time], (0,4410), mode='constant')



from librosa.onset import onset_strength


def compute_t_v(mix,nov,time):

    vocal = mute_start(mix[:time])
    no_vocal = nov[:time]

    # step 1

    a = onset_strength(vocal)
    b = onset_strength(no_vocal)
    sample_onset_ratio = int(nov[:time].shape[0]/b.shape[0])

    # step 2

    onset_shift = npp.find_shift(a,b)
    sample_shift = onset_shift * sample_onset_ratio

    # vocal = npp.right_shift(vocal,sample_shift)

    fine_sample_shift = npp.find_shift(vocal,no_vocal)

    # compute volume

    vol_ratio = LA.norm(vocal)/LA.norm(no_vocal)

    print(vol_ratio)

    return fine_sample_shift, vol_ratio





if __name__ == "__main__":

    mix, sr = librosa.load("test_data/小幸運-有人聲.mp3", sr=None)
    nov, sr = librosa.load("test_data/小幸運-純伴奏.mp3", sr=None)
    voc, sr = librosa.load("test_data/小幸運-純人聲版.mp3", sr=None)

    # 計算位移，音量
    shift, vol = compute_t_v(mix,nov,time)

    # mix2 = mix[:882000]
    # nov2 = nov[:882000]

    mix,nov = npp.pad_the_same(mix,nov)


    # plt.plot(mix2)
    mix2 = npp.right_shift(mix,shift)
    # plt.plot(mix2)
    # plt.plot(nov2)

    result = mix2*1.5 - nov
    librosa.output.write_wav("res.wav", result, sr)