from numpy.core.fromnumeric import searchsorted
import DataReader
import matplotlib.pyplot as plt
params = {
    #'text.usetex' : True,
    'font.size' : 18,
    'font.serif' :'cm',
    #'text.latex.unicode': True
}
plt.rcParams.update(params)

directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\SARLines\\SAR.out\\'

df_x = df = DataReader.get_all_data(directory+'alongx.txt',printtf=False)
df_z = df = DataReader.get_all_data(directory+'alongz.txt',printtf=False)

def plot_hysteresis(df_x,df_y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(df_x['B_ext_z'][:]*10**3,df_x['<mz>'][:],label='x')
    ax.plot(df_z['B_ext_z'][:]*10**3,df_z['<mz>'][:],label='z')
    
    ax.set_xlabel('Applied field [mT]')
    ax.set_ylabel('Magnetization')
    ax.legend()
    plt.show()
    
plot_hysteresis(df_x,df_z)