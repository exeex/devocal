from lyric_parser import lyric
import librosa
import matplotlib.pyplot as plt


aud, sr = librosa.load("test_data/小幸運-消人聲版.mp3", sr=None)
l = lyric("test_data/lyric.txt")
items = l.parse(l.text)

def ms2sample(time_ms):

    time_sample = int(round(time_ms /1000 * sr,0))

    return time_sample


new_seq = []

# for item in items:
#     try:
#         start, duration, char = item
#         start = ms2sample(start)
#         duration = ms2sample(duration)
#         aud_char = aud[start:start+duration]
#         # chroma = librosa.feature.chroma_stft(aud_char)
#
#         new_seq.append((start,duration,char,aud_char))
#     except Exception as e:
#         print(e)

