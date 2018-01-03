import librosa
import lyric_parser
import matplotlib.pyplot as plt
import numpy as np


mix, sr = librosa.load("test_data/小幸運-有人聲.mp3", sr=None)
nov, sr = librosa.load("test_data/小幸運-純伴奏.mp3", sr=None)
voc, sr = librosa.load("test_data/小幸運-純人聲版.mp3", sr=None)



def ms2sample(time_ms):

    time_sample = int(round(time_ms /1000 * sr, 0))

    return time_sample

def mute_start(sig):
    sig[0:1000] = 0
    return sig

time = lyric_parser.l.get_time_before_vocal()


time = ms2sample(time)

# r = librosa.zero_crossings(voc[0:time])

# pad = np.pad(mix[:time],(0,4410), mode='constant')

# con = np.convolve(pad,nov[0:time], mode='valid')

# plt.plot(con)

# r = librosa.logamplitude(librosa.feature.melspectrogram(voc[time:time*3],sr=sr,n_fft=4096,hop_length=2048))
#
# # voc[0:time]




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

a = onset_strength(mute_start(mix[:time])) 
b = onset_strength(nov[:time])

plt.plot(a)
plt.plot(b)

con1 = np.convolve(onset_strength(mix[:time]), onset_strength(nov[:time]), mode='same')

# con2 = np.convolve(onset_strength(nov[:time]), onset_strength(mix[:time]), mode='same')

# plt.plot(con1)
# plt.plot(con2)



# x = linspace(0,4,1e3)
# data = .2*sin(10*x)+ exp(-abs(2-x)**2)



# that's the line, you need:
# a = diff(sign(diff(data))).nonzero()[0] + 1 # local min+max
# b = (diff(sign(diff(data))) > 0).nonzero()[0] + 1 # local min
# c = (diff(sign(diff(data))) < 0).nonzero()[0] + 1 # local max
#
# # graphical output...
# x=np.array(list(range(len(data))))
# plt.plot(x,data)
# plt.plot(x[b], data[b], "o", label="min")
# plt.plot(x[c], data[c], "o", label="max")
# plt.legend()
# plt.show()