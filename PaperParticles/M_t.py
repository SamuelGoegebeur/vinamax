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
file = 'd20_µ033_B25.txt'


df = DataReader.get_all_data(directory+file,printtf=True)
#DFPlotter.plotter(df)

def M(df,x='H'):
    
    if x=='t':
        fig, ax = plt.subplots()
        ax.plot(df["#t"]*10**6,df['<mx>'],color='red',label='M')
        ax.set_xlabel('Time [µs]')
        ax.set_ylabel('Magnetization') 
        
        ax2 = plt.twinx(ax)
        ax2.set_ylabel('Applied field [mT]')
        ax2.legend(loc=1)
        
    if x=='H':
        fig, ax = plt.subplots()
        ax.plot(df['B_ext_x'][:]*10**3,df['<mx>'][:])
        ax.set_xlabel('Applied field [mT]')
        ax.set_ylabel('Magnetization')
        
    if x=='tH':
        fig = plt.figure()
        fig.suptitle(file)
        ax = fig.add_subplot(1,2,1)
        ax.plot(df["#t"]*10**6,df['B_ext_x']*10**3,color='blue',label = 'B')
        ax.set_ylabel('Applied field [mT]')
        ax.set_xlabel('Time [µs]')
        ax.set_yticks([-25,-15,-5,5,15,25])
        ax.set_yticklabels([-25,-15,-5,5,15,25])
        ax.legend(loc=2)
        
        ax2 = plt.twinx(ax)
        ax2.plot(df["#t"]*10**6,df['<mx>'],color='red',label='M')
        ax2.set_ylim(-1,1)
        
        ax2.set_ylabel('Magnetization')
        ax2.legend(loc=1)
        
                   
        
        
        ax3 = fig.add_subplot(1,2,2)
        ax3.plot(df['B_ext_x'][:]*10**3,df['<mx>'][:])
        ax3.set_xlabel('Applied field [mT]')
        ax3.set_xticks([-25,-15,-5,5,15,25])
        ax3.set_xticklabels([-25,-15,-5,5,15,25])
        ax3.set_ylim(-1,1)
        
        fig.subplots_adjust(top = 0.845 , bottom = 0.160, left = 0.115, right = 0.965,hspace=0, wspace = 0.5)

    plt.show()

M(df,x='tH')