import librosa
import lyric_parser
import matplotlib.pyplot as plt
mix, sr = librosa.load("test_data/小幸運-有人聲.mp3", sr=None)
nov, sr = librosa.load("test_data/小幸運-純伴奏.mp3", sr=None)
voc, sr = librosa.load("test_data/小幸運-純人聲版.mp3", sr=None)



def ms2sample(time_ms):

    time_sample = int(round(time_ms /1000 * sr,0))

    return time_sample

time = lyric_parser.l.get_time_before_vocal()


time = ms2sample(time)

# r = librosa.zero_crossings(voc[0:time])

r = librosa.logamplitude(librosa.feature.melspectrogram(voc[time:time*3],sr=sr,n_fft=4096,hop_length=2048))

# voc[0:time]