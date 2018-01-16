import librosa
import lyric_parser
# import matplotlib.pyplot as plt
from numpy import linalg as LA
# import numpy as np
import npp
from librosa.onset import onset_strength



def ms2sample(time_ms, sr=44100):
    time_sample = int(round(time_ms / 1000 * sr, 0))

    return time_sample


def mute_start(sig):
    sig[0:1000] = 0
    return sig


def compute_t_v(mix, bg, time):

    mix = mix[:time]
    bg = bg[:time]

    # compute shift


    fine_sample_shift = npp.find_shift(mix, bg)

    # compute volume

    vol_ratio = LA.norm(bg) / LA.norm(mix)

    print(vol_ratio)

    return fine_sample_shift, vol_ratio


if __name__ == "__main__":

    # 讀audio檔
    mix, sr = librosa.load("test_data/小幸運-有人聲.mp3", sr=None)
    nov, sr = librosa.load("test_data/小幸運-純伴奏.mp3", sr=None)

    # 取得前奏的時間
    time = lyric_parser.l.get_time_before_vocal()

    # 單位變換，從ms換成sample
    time = ms2sample(time - 1000)
    time = time // 2

    # 前處理
    mix = mute_start(mix)
    nov = mute_start(nov)

    # 計算位移，音量
    shift, vol = compute_t_v(mix, nov, time)

    # 前處理
    mix, nov = npp.pad_the_same(mix, nov)
    mix2 = npp.right_shift(mix, shift)

    # 訊號相減
    result = mix2 * vol - nov

    # 輸出
    librosa.output.write_wav("res.wav", result, sr)
