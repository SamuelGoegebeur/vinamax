import numpy as np
from scipy import linalg
from scipy.special import eval_chebyu
import matplotlib.pyplot as plt
import seaborn as sns

import DataReader
import Voltage

def measurement_systemfunction(S_meas):
    S = np.zeros((S_meas.N,S_meas.M-1),dtype="complex_")

    for k in range(1,S_meas.M):
        #Iteration over all files to be added to the systemfunction S
        x = (-S_meas.X_scan + 2*S_meas.X_scan*k/(S_meas.M))*1e3
        x = "{:.3f}".format(x)
        file = '101MNPs_of_radius30_@x{}mm.txt'.format(x)
        df = DataReader.get_all_data(S_meas.directory+file,printtf=False)
        _,spectrum = Voltage.voltage_FFT(df,S_meas.N)
        S[:,k-1] = spectrum
    return S

def invert_S(S,rcond=1e-2):
    S_inv = linalg.pinv(S,rcond=rcond)
    return S_inv

def x_space_frequency(N):
    #index n in systemfunction ranges from 1-N, not from zero!!
    #zerots row of S is left unchanged
    M = 1000
    x = np.linspace(-2.4e-3,2.4e-3,M)
    G = 5       #T/m
    A = 12e-3      #mT
    T = 40e-6
    M0 = 1
    S = np.zeros((N,M),dtype="complex_")
    for n in range(1,N):
        Un_min1 = eval_chebyu(n-1,G*x/A)
        S[n,:] = -4j*M0/T*Un_min1*np.sqrt(1-(G*x/A)**2)
    return S

def invert_S_xspace(S):
    M = 1000
    x = np.linspace(-2.4e-3,2.4e-3,M)
    G = 5       #T/m
    A = 12e-3      #mT
    T = 40e-6
    M0 = 1
    alpha = -2/np.pi*G/A*(T/4*M0)**2
    beta = np.diag(1/np.sqrt(1-(G*x/A)**2))
    S_inv = alpha*np.matmul(beta,S.transpose())
    plt.figure()
    sns.heatmap(np.abs(np.matmul(S_inv,S)))
    plt.show()
    return S_inv









