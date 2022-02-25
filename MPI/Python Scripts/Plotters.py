import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

params = {
    #'text.usetex' : True,
    'font.size' : 14,
    'font.serif' :'cm',
    #'text.latex.unicode': True
}
plt.rcParams.update(params)

def voltage_plot(t,phi,u):
        fig,ax = plt.subplots()
        ax.plot(t[:]*10**6,phi[:],color='blue',label="Flux")
        ax.set_ylabel('Magnetic flux [Wb]')
        ax.legend(loc=2)

        ax2 = plt.twinx(ax)
        ax2.plot(t[:-1]*10**6,u,color='red',label='Voltage')
        ax2.set_ylabel('Voltage [V]')
        ax2.legend(loc=1)

        ax.set_xlabel('Time [µs]')
        plt.title('Magnetic flux and voltage at coil')

        #plt.figtext(0.5, 0.01, "For the moment coil means 1 point", ha="center", fontsize=12)
        plt.show()

def voltage_FFT_plot(freq,spectrum):
    fig, axs = plt.subplots(3, sharex=True, sharey=True)

    N = len(freq)
    axs[0].bar(freq/freq[1], np.real(spectrum),label='Real',color='red')
    axs [0].legend()
    axs[1].bar(freq/freq[1], np.imag(spectrum),label='Imag',color='green')
    axs[1].legend()
    axs[2].bar(freq/freq[1], np.abs(spectrum),label='Abs')
    plt.xticks(freq/freq[1])
    plt.xlabel('Harmonics')
    print(freq)
    plt.legend()
    plt.show()

def systemfucntion_sns(S,S_inv):
    plt.figure()
    sns.heatmap(np.abs(S))
    plt.title('Systemfunction')
    plt.xlabel('x_coordinate')
    plt.ylabel('frequencies')
    plt.show()
    plt.figure()
    sns.heatmap(np.abs(S_inv))
    plt.title('Invere systemfunction')
    plt.show()

def concentrationprofile(x,c_calc,x_input,c_input):
    fig,ax = plt.subplots()
    ax.plot(x*1e3,c_calc,color='red',label='MPI signal')
    ax.plot(x_input*1e3,c_input,color='black',label='Original')
    ax.set_xlabel('x [mm]')
    ax.legend()
    plt.show()

def systemfct_freq(x,S):
    fig,axs = plt.subplots(2,2)
    fig.suptitle('systemfunction frequency components')
    axs[0,0].plot(x*1e3,np.abs(S[3,:])/np.max(np.abs(S[2,:])),label='3')
    axs[0,1].plot(x*1e3,np.abs(S[6,:])/np.max(np.abs(S[6,:])),label='6')
    axs[1,0].plot(x*1e3,np.abs(S[12,:])/np.max(np.abs(S[12,:])),label='12')
    axs[1,1].plot(x*1e3,np.abs(S[18,:])/np.max(np.abs(S[18,:])),label='18')
    axs[0,0].set_xlabel("x [mm]")
    axs[0,0].legend()
    axs[0,1].set_xlabel("x [mm]")
    axs[0,1].legend()
    axs[1,0].set_xlabel("x [mm]")
    axs[1,0].legend()
    axs[1,1].set_xlabel("x [mm]")
    axs[1,1].legend()
    #plt.ylabel('abs value')
    
    plt.show()  