import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import DataReader

def plot_df(file,title):
    df = DataReader.get_all_data(file)
    fig,ax = plt.subplots()
    ax.set_title(title)
    sns.heatmap(df)
    ax.set_xlabel("x [mm]")
    ax.set_ylabel('Time [µs]')
    plt.show()

def input(x,c):
    C = np.zeros(len(x))
    for i in c:
        idx = np.where(np.abs(x*1e3-i)<1e-2)[0]
        C[idx] = 1
        if (len(idx) == 0):
            idx = np.where(np.abs(x*1e3-i)==np.min(np.abs(x*1e2-i)))[0]
            x[idx] = i*1e-3
            C[idx] = 1
    return C

def Concentrationprofile(x,C,c_orig):
    C_orig = input(x,c_orig)
    plt.figure()
    plt.plot(x*1e3,C,color='red',label='Reconstruction')
    plt.plot(x*1e3,C_orig,color='black',label='Input')
    plt.xlabel('x [mm]')
    plt.ylabel('Concentrationprofile')
    plt.legend()
    plt.show()

def Voltage(t,V,V_orig):
    plt.figure()
    plt.plot(t*1e6,V,color='red',label='Reconstruction')
    plt.plot(t*1e6,V_orig,color='black',label = 'Measured voltage')
    plt.xlabel('Time [µs]')
    plt.ylabel('Voltage')
    plt.legend()
    plt.show()
