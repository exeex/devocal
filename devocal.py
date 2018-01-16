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


def get_vocal(mix_file,bg_file,lyric_file,out_file="out.wav"):
    # 讀audio檔
    mix, sr = librosa.load(mix_file, sr=None)
    bg, sr = librosa.load(bg_file, sr=None)

    # 取得前奏的時間
    l = lyric_parser.lyric(lyric_file)
    time = l.get_time_before_vocal()

    # 單位變換，從ms換成sample
    time = ms2sample(time - 1000, sr)
    time = time // 2

    # 前處理
    mix = mute_start(mix)
    bg = mute_start(bg)

    # 計算位移，音量
    shift, vol = compute_t_v(mix, bg, time)

    # 前處理
    mix, bg = npp.pad_the_same(mix, bg)
    mix2 = npp.right_shift(mix, shift)

    # 訊號相減
    result = mix2 * vol - bg

    # 輸出
    librosa.output.write_wav(out_file, result, sr)


if __name__ == "__main__":

    get_vocal("test_data/小幸運-有人聲.mp3","test_data/小幸運-純伴奏.mp3","test_data/Lyric.txt","out.wav")
