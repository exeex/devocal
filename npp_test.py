import numpy as np
from npp import *


if __name__ == "__main__":

    #### test pad fxns and get a1,a2

    a = np.zeros((5))

    a += 1

    a = left_pad(a,20)

    a = right_pad(a,10)


    b = np.array((1.,2.,3.,4.))


    a1 = a
    a2 = right_shift(a,5)


    #### test convolve fxn
    #
    # print(a1)
    # print(a2)
    #
    # left,right = convolve(a1,a2)
    #
    # print(left)
    # print(right)


    #### test find_shift
    #
    # a1 = right_shift(a1,-4)
    #
    # print(a1)
    # print(a2)
    #
    # shift = find_shift(a1,a2)
    #
    # # print(type(shift))
    # a1 = right_shift(a1,shift)
    #
    # print(find_shift(a1,a2))

    #### test auto_shift

    # a1 = right_shift(a1,5)

    print(a2)
    print(a1)

    a2 = auto_shift(a2,a1)
    print(a2)


    ##

# if __name__ == "__main__":
#     import matplotlib.pyplot as plt
#     import librosa
#     from librosa.onset import onset_strength
#     import lyric_parser
#
#     mix, sr = librosa.load("test_data/小幸運-有人聲.mp3", sr=None)
#     nov, sr = librosa.load("test_data/小幸運-純伴奏.mp3", sr=None)
#     voc, sr = librosa.load("test_data/小幸運-純人聲版.mp3", sr=None)
#
#     def ms2sample(time_ms):
#         time_sample = int(round(time_ms / 1000 * sr, 0))
#
#         return time_sample
#
#
#     def mute_start(sig):
#         sig[0:1000] = 0
#         return sig
#
#
#     time = lyric_parser.l.get_time_before_vocal()
#
#     time = ms2sample(time)
#
#     a = onset_strength(mute_start(mix[:time]))[250:350]
#     a_ = right_shift(a,-30)
#     # b = onset_strength(nov[:time])
#     #
#     # a = np.clip(a, 2, 10) - 2
#     # b = np.clip(b, 2, 10) - 2
#     # print(a,a_)
#
#
#     _, a2 = convolve(a_, a)
#
#     plt.plot(a)
#     plt.plot(a_)
#     plt.plot(a2)