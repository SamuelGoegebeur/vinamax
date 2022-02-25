import numpy as np
import matplotlib.pyplot as plt

import DataReader
import Voltage
import Systemfunction
import Plotters
import Concentrationprofiles

dir_systemfunctions = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\Systemfunction\\'
dir_phantoms = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\1D.out\\'

class Systemfunction_measurement:
    "Contains info and location of the measured systemfunction"
    #S_meas
    def __init__(self,N,M,X_scan,directory):
        self.directory = directory
        self.N = N              #Nr of frequencies
        self.M = M              #Nr of measurements of systemfunction
        self.X_scan = X_scan    #Range of measuement [mm]

class Phantom:
    def __init__(self,file,c):
        self.file = file
        self.c = c         #list with location of MNPs

k30 = Systemfunction_measurement(20,30,2.4e-3,dir_systemfunctions+'30 steps\\')
k50 = Systemfunction_measurement(20,50,2.4e-3,dir_systemfunctions+'\\50 steps\\')
phantom1 = Phantom(dir_phantoms+'1Particle1.5.txt',[1.5])
#phantom1 = Phantom(dir_phantoms+'1Particle1.5_demagtrue.txt',[1.5])
phantom2 = Phantom(dir_phantoms+'2Particles0.75.txt',[-0.75,0.75])
phantom3 = Phantom(dir_phantoms+'3Particles_-2_0.15_1.5.txt',[-2,0.15,1.5])
phantom0 = Phantom(dir_systemfunctions+'50 steps\\'+'101MNPs_of_radius30_@x0.000mm.txt',[0.00])


def plot_voltage(phantom,N):
    df = DataReader.get_all_data(phantom.file,printtf=False)
    t,_,phi,u = Voltage.voltage_timedomain(df)
    freq,spectrum = Voltage.voltage_FFT(df,N)
    Plotters.voltage_plot(t,phi,u)
    Plotters.voltage_FFT_plot(freq,spectrum)

def measurement_based(system,phantom):
    x = Concentrationprofiles.x_axis(system)
    S = Systemfunction.measurement_systemfunction(system)
    S_inv = Systemfunction.invert_S(S,rcond=0.1)
    df_phantom = DataReader.get_all_data(phantom.file,printtf=False)
    freq,U_meas = Voltage.voltage_FFT(df_phantom,system.N)
    c_calc = Concentrationprofiles.calculated(S_inv,U_meas) #real,imag abs
    x_input,c_input = Concentrationprofiles.input(x,phantom)
    Plotters.concentrationprofile(x,c_calc,x_input,c_input)
    Plotters.systemfct_freq(x,S)
    Plotters.systemfucntion_sns(S,S_inv)

def x_space(N,phantom):
    
    df_phantom = DataReader.get_all_data(phantom.file,printtf=False)
    freq,U_meas = Voltage.voltage_FFT(df_phantom,N)
    S = Systemfunction.x_space_frequency(N)
    x,c = Concentrationprofiles.x_space_frequency(N,S,U_meas)
    #Plotters.concentrationprofile(x,c,0,0)
    S_inv = Systemfunction.invert_S_xspace(S[1:])
    c_calc  = Concentrationprofiles.calculated(S_inv,U_meas[1:])
    plt.figure()
    plt.plot(x,c)
    plt.show()

    #Plotters.systemfucntion_sns(S,S)
    #Plotters.voltage_FFT_plot(freq,U_meas)



#plot_voltage(phantom0,20)
#measurement_based(k50,phantom0)
x_space(20,phantom0)