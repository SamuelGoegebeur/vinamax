import numpy as np
from scipy.fftpack import fftfreq,fft
import matplotlib.pyplot as plt

import Plotters

def x_axis(S_meas):
    x = []
    for k in range(1,S_meas.M):
        x.append(-S_meas.X_scan + 2*S_meas.X_scan*k/S_meas.M)
    x = np.array(x)
    return x

def calculated(S_inv,U_meas):
    C_calc = np.abs(np.matmul(S_inv,U_meas))
    return C_calc/np.max(C_calc)

def c_x(x,freq,c):
    N = len(x)
    freq = fftfreq(N,x[1]-x[0])[:]
    c1 = 2/N*fft(c)[:]
    c_x =0    
    y = len(freq)
    for i in range(y-1):
        c_x += c1[i]*np.exp(2j*np.pi*x*freq[i])
    return c1

def input(x,phantom):
    c = np.zeros(len(x))
    for i in phantom.c:
        idx = np.where(np.abs(x*1e3-i)<1e-3)[0]
        c[idx] = 1
        if (len(idx) == 0):
            idx = np.where(np.abs(x*1e3-i)==np.min(np.abs(x*1e3-i)))[0]
            x[idx] = i*1e-3
            c[idx] = 1
        #c[idx-1] = 1
        #c[idx+1] = 1
    return x,c

def x_space_frequency(N,S,U):
    x = np.linspace(-2.4e-3,2.4e-3,1000)
    G = 5
    A = 12e-3
    T = 40e-6
    M0 = 1
    c = 0+0j
    for n in range(1,N):
        c += S[n]*(U[n])
    c = np.real(-2/np.pi*G/A*(T/4/M0)**2*1/np.sqrt(1-(G*x/A)**2)*c)
    return x,c