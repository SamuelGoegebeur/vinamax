import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import seaborn as sns


import DataReader
import Voltage
import Xspace
import Xspace_Plotters

S_directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\results\\'
U_directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\1D.out\\'
S_file = S_directory+'S.txt'
U_file = U_directory+'articles1.5_r10.txt'

#U_file = U_directory+'k30\\101MNPs_of_radius30_@x0.000mm.txt'

N = 2000
M = 1000

t = np.linspace(0,160e-6,N)
x = np.linspace(-2.4e-3,2.4e-3,M)

def init(S_file,U_file,cut):
    S = DataReader.get_all_data(S_file).to_numpy(dtype=float)
    t_U,_,_,U_meas = Voltage.voltage_timedomain(U_file,plot_fit=True)
    itp = interp1d(t_U[:-1],U_meas)
    U = itp(t[cut[0]:cut[1]])

    return t[cut[0]:cut[1]],S[cut[0]:cut[1],:],U

#Xspace_Dataframes.plot_df(S_file,'S')

t,S,U = init(S_file,U_file,cut = [N//4,-N//4])
U /= np.max(U)
S /= np.max(S)

C = Xspace.Kaczmarz(10,S,U)
Xspace_Plotters.Voltage(t,np.matmul(S,C)/np.max(np.matmul(S,C)),U)
Xspace_Plotters.Concentrationprofile(x,C,[2.0])
