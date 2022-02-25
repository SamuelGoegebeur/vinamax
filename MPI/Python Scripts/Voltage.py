import numpy as np
from scipy.fftpack import fft, fftfreq,ifft,rfft,rfftfreq,irfft
import Savitzky_golay
import matplotlib.pyplot as plt

import DataReader

def voltage_timedomain(file,high_noise=True,plot_fit=False):
    df = DataReader.get_all_data(file,printtf=False)
    t = df['#t']
    dt = 1.6e-7
    phi = np.array(df['B_x@(0.2,0,0)'])

    phi_smooth,u_smooth = Timedomain_filter(t,dt,phi)
    #phi_smooth,u_smooth = FFT_filter(t,dt,phi)

    return t,dt,phi_smooth,u_smooth

def Timedomain_filter(t,dt,phi,high_noise=False,plot_fit=True):
    if high_noise:
        phi_smooth = Savitzky_golay.savitzky_golay(phi, 30, 1) #smooth the signal
        phi_smooth = Savitzky_golay.savitzky_golay(phi_smooth, 10, 1)
        u = -(phi_smooth[1:]-phi_smooth[:-1])/dt
        u_smooth = Savitzky_golay.savitzky_golay(u, 10, 1)

    else:
        phi_smooth = Savitzky_golay.savitzky_golay(phi, 5, 1) #smooth the signal
        u = -(phi_smooth[1:]-phi_smooth[:-1])/dt
        u_smooth = Savitzky_golay.savitzky_golay(u, 3, 1)

    if plot_fit:
        fig,ax = plt.subplots(1,2)
        fig.suptitle('Preprocessing flux and voltage')
        ax[0].plot(t*1e6,phi,label='Orginal')
        ax[0].plot(t*1e6,phi_smooth,label='Smooth')
        ax[1].plot(t[:-1]*1e6,u,label='Original')
        ax[1].plot(t[:-1]*1e6,u_smooth,label='Smooth')
        plt.show()

    return phi_smooth,u_smooth

def FFT_filter(t,dt,phi):
    N = len(t)

    w = rfft(phi)
    f = rfftfreq(N, dt)
    spectrum = w**2

    cutoff_idx = spectrum < (spectrum.max()/1e3)
    w2 = w.copy()
    w2[cutoff_idx] = 0

    y2 = irfft(w2)
    phi_smooth = Savitzky_golay.savitzky_golay(phi, 5, 1)
    u = -(phi_smooth[1:]-phi_smooth[:-1])/dt
    u_smooth = Savitzky_golay.savitzky_golay(u, 3, 1)
    
    print(y2)
    plt.figure()
    plt.plot(t,phi)
    plt.plot(t,y2)
    plt.plot(t,phi_smooth)
    plt.show()

    return phi_smooth,u_smooth


def voltage_FFT(df,cutoff):
    _,dt,_,u = voltage_timedomain(df)
    T = dt
    
    u = u[3*len(u)//4:]
    N = len(u)
    freq = fftfreq(N, T)[:N//2][:cutoff]
    spectrum = 2/N*fft(u)[:N//2][:cutoff]
    
    return freq,spectrum

def make_odd(t,u):
    close_to_zeros = np.where(u[:-1]*u[1:]<0)[0]
    close_to_zeros = close_to_zeros[np.where(np.sign(u[close_to_zeros])<0)[0]]
    
    min,max = close_to_zeros[2],close_to_zeros[2]+250
    plt.figure()
    #plt.plot(t[:-1],u)
    plt.scatter(t[:-1][min:max],u[min:max])
    plt.show()

    return t[:-1][min:max],u[min:max]

