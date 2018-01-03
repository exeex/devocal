import numpy as np


def left_pad(array,pad_length):

    if pad_length >= 0:
        return np.pad(array, (pad_length, 0), "constant", constant_values=(0, 0))
    elif pad_length < 0:
        return array[[-pad_length]:]


def right_pad(array,pad_length):

    if pad_length >= 0:
        return np.pad(array,(0,pad_length),"constant", constant_values=(0, 0))
    elif pad_length < 0:
        return array[:[pad_length]]


def right_shift(array,length):

    return left_pad(right_pad(array,-length),length)


def left_shift(array, length):

    return left_pad(right_pad(array, length), -length)




def convolve(kernel_array, array):

    print(array.shape[0])

    convolved = np.convolve(kernel_array, array)
    print(convolved)
    right = convolved[::-1].copy()
    right = right[kernel_array.shape[0]-2:]
    right = right[:array.shape[0]]

    left = convolved.copy()
    left = left[kernel_array.shape[0]:]

    return left, right


if __name__ == "__main__":


    a = np.zeros((5))

    a += 1

    a = left_pad(a,2)

    a = right_pad(a,3)


    b = np.array((1.,2.,3.,4.))


    a1 = right_pad(a,2)
    print(a1.shape)
    a2 = left_pad(a,2)


    print(a1)
    print(a2)

    left,right = convolve(a1,a2)

    print(left)
    print(right)
