import numpy as np


def raw_to_fourier(df, fs):

    col = len(df.columns)
    fft_lst = []
    freq_lst = []

    for i in range(col):

        df_col = df.iloc[:, [i]]

        n = len(df_col)
        k = np.arange(n)
        Fs = fs
        T = n/Fs
        freq = k/T
        freq = freq[range(int(n))]

        Y = np.fft.fft(df_col)/n

        Y = Y[range(int(n/2))]

        abs_Y = abs(Y) ** 2

        fft_lst.append(abs_Y)
        freq_lst.append([freq])

    return fft_lst, freq_lst
