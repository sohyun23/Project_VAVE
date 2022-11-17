import numpy as np

def raw_to_fourier(df, fs):
    
    fft_lst = []

    iter = len(df.columns)
    n = len(df)

    k = np.arange(n) 
    Fs = fs
    T = n/Fs 
    freq = k/T
    freq = freq[range(int(n))]

    for i in range(iter):
        
        df_col = df.iloc[:, [i]]

        Y = np.fft.fft(df_col)/n
        
        Y = Y[range(int(n/2))]

        abs_Y = abs(Y) ** 2 

        fft_lst.append(abs_Y)

    return fft_lst, freq