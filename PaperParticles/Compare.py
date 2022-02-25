from numpy.core.fromnumeric import searchsorted
import DataReader
import DFPlotter
import matplotlib.pyplot as plt
params = {
    #'text.usetex' : True,
    'font.size' : 18,
    'font.serif' :'cm',
    #'text.latex.unicode': True
}
plt.rcParams.update(params)

directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\PaperParticles\\Hysteresis.out\\'

df_98 = df = DataReader.get_all_data(directory+'d98_µ063_B25.txt',printtf=False)
df_50 = df = DataReader.get_all_data(directory+'d50_µ033_B25.txt',printtf=False)
df_20 = df = DataReader.get_all_data(directory+'d20_µ033_B25.txt',printtf=False)

def plot_hysteresis(df_20,df_50,df_98):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(df_20['B_ext_x'][:]*10**3,df_20['<mx>'][:],label=20)
    ax.plot(df_50['B_ext_x'][:]*10**3,df_50['<mx>'][:],label=50)
    ax.plot(df_98['B_ext_x'][:]*10**3,df_98['<mx>'][:], label=98)
    ax.set_xlabel('Applied field [mT]')
    ax.set_ylabel('Magnetization')
    ax.legend()
    plt.show()
    
plot_hysteresis(df_20,df_50,df_98)