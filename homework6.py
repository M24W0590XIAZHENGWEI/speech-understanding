import numpy as np
import matplotlib.pyplot as plt

def minimum_Fs(f):
    '''
    Find the lowest sampling frequency that would avoid aliasing for a pure tone at f Hz.
    '''
    Fs = 2 * f
    return Fs

def omega(f, Fs):
    '''
    Find the radial frequency (omega) that matches a given f and Fs.
    '''
    omega = 2 * np.pi * f / Fs
    return omega

def pure_tone(omega, N):
    '''
    Create a pure tone of N samples at omega radians/sample.
    '''
    n = np.arange(N)
    x = np.cos(omega * n)
    return x

# ====== テストコード ======
if __name__ == "__main__":
    f = 440  # Hz
    Fs = minimum_Fs(f)
    print(f"Minimum sampling frequency to avoid aliasing: {Fs} Hz")

    w = omega(f, Fs)
    print(f"Radial frequency omega: {w} radians/sample")

    N = 200
    x = pure_tone(w, N)

    # 波形表示
    plt.plot(x)
    plt.title(f"Pure Tone: {f} Hz, Sampled at {Fs} Hz")
    plt.xlabel("Sample Number")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
