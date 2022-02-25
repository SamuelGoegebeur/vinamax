from numpy.core.fromnumeric import searchsorted
import DataReader
import matplotlib.pyplot as plt
import numpy as np
params = {
    #'text.usetex' : True,
    'font.size' : 14,
    'font.serif' :'cm',
    #'text.latex.unicode': True
}
plt.rcParams.update(params)

directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\1D.out\\'
file = '1Particle1.5.txt'


df = DataReader.get_all_data(directory+file,printtf=False)

def plot_DriveField(df,loc='0.001'):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax2 = plt.twinx(ax)

    ax.plot(df["#t"]*10**6,df['B_ext_space_x_-'+loc]*10**3,color='red',label='-Xscan')
    ax.plot(df["#t"]*10**6,df['B_ext_space_x_0']*10**3,color='blue',label='Origin')
    ax.plot(df["#t"]*10**6,df['B_ext_space_x_'+loc]*10**3,color='green',label='Xscan')
    
    ax2.plot(df['#t']*10**6,df['FFP_x']*10**3,alpha=0.5,linewidth=3)
    ax2.set_ylabel("FFP [mm]")
    ax2.grid()

    ax.set_ylabel('Applied Field [mT]') 
    ax.set_xlabel('Time [µs]')
    ax.grid()
    ax.legend(loc=1,fontsize='x-large')
    plt.show()


def plot_Field(df,loc='@(1e-07,0,0)'):
    fig = plt.figure()
    #ax = fig.add_subplot(311)
    ax2 = fig.add_subplot(211)
    ax3 = fig.add_subplot(212)

    #ax.plot(df["#t"]*10**6,df['B_ext_space_x'],color='red',label='B')
    ax2.plot(df['#t'][:]*10**6,df['B_x'+loc][:])
    ax3.plot(df['#t'][:]*10**6,df['<mx>'][:])
    

    #ax.set_ylabel('Bdrive\n@origin') 
    ax2.set_ylabel('B'+loc)
    ax3.set_ylabel('mx')
    
    #ax.set_xticklabels([])
    ax2.set_xticklabels([])
    ax3.set_xlabel('Time [µs]')

    #ax.grid()
    ax2.grid()
    ax3.grid()

      
    plt.show()


#plot_DriveField(df,loc='0.0024')     #loc = Xscan e06 not e6!!
plot_Field(df,loc='@(0.2,0,0)')  #loc = first coil
#show FFP, field strength and B at first coil vs m total
