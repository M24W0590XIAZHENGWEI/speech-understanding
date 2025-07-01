import numpy as np

def fourier_synthesis(num_harmonics, X, T0):
    '''
    Use Fourier synthesis to resynthesize speech from its Fourier transform.
    
    x[n] = (2/N) * sum_{l=1}^{num_harmonics} |X[l*N//T0]| * cos(2*pi*l*n/T0 + angle(X[l*N//T0]))
    '''
    N = len(X)
    x = np.zeros(N)

    for n in range(N):
        sum_harmonics = 0
        for l in range(1, num_harmonics + 1):
            k = l * N // T0  # harmonic index in DFT
            if k >= N:
                continue  # prevent out-of-bounds
            magnitude = np.abs(X[k])
            phase = np.angle(X[k])
            sum_harmonics += magnitude * np.cos(2 * np.pi * l * n / T0 + phase)
        x[n] = (2 / N) * sum_harmonics

    return x
