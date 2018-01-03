import numpy as np


def left_pad(array,pad_length):

    if pad_length >= 0:
        return np.pad(array, (pad_length, 0), "constant", constant_values=(0, 0))
    elif pad_length < 0:
        return array[-pad_length:].copy()


def right_pad(array,pad_length):

    if pad_length >= 0:
        return np.pad(array,(0,pad_length),"constant", constant_values=(0, 0))
    elif pad_length < 0:
        return array[:pad_length]


def right_shift(array,length):
    buf = right_pad(array, -length)
    return left_pad(buf,length)


def left_shift(array, length):
    buf = left_pad(array, -length)
    return right_pad(buf, length)




def convolve(kernel_array, array):


    convolved = np.convolve(kernel_array[::-1], array)
    print(convolved)
    right = convolved.copy()
    right = right[kernel_array.shape[0]-1:]

    left = convolved.copy()
    left = left[:kernel_array.shape[0]][::-1]

    return left, right


def find_shift(kernel_array:np.ndarray, array:np.ndarray):
    left, right = convolve(kernel_array, array)

    # print(left)
    # print(right)


    r_max_idx = np.argmax(right)
    r_max_value = right.max()

    l_max_idx = np.argmax(left)
    l_max_value = left.max()

    print(r_max_idx,r_max_value)
    print(l_max_idx,l_max_value)

    # return int(r_max_idx)
    if r_max_value > l_max_value:
        return int(r_max_idx)
    else:
        return int(-l_max_idx)

def auto_shift(kernel_array:np.ndarray, array:np.ndarray):

    shift = find_shift(kernel_array,array)
    a1 = right_shift(kernel_array,shift)
    print(shift)
    # print(find_shift(a1,a2))

    return a1

if __name__ == "__main__":


    a = np.zeros((5))

    a += 1

    a = left_pad(a,2)

    a = right_pad(a,3)


    b = np.array((1.,2.,3.,4.,5.))


    a1 = right_pad(a,2)
    a2 = left_pad(a,3)


    # print(b)
    # print(a1)
    # #
    # left,right = convolve(b,a1)
    #
    # print(left)
    # print(right)
    # print(np.convolve(a2,a1))

    print(a2)
    print(a1)

    a2 = auto_shift(a2,a1)
    print(a2)