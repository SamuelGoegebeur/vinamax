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


directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\'
file = 'tryouts\\Lognormal.out\\table.txt'
#file = 'tryouts\\Lognormal.out\\geometry000000.txt'

df = DataReader.get_all_data(directory+file,printtf=True)
#DFPlotter.plotter(df)

fig, ax = plt.subplots()
ax2 = plt.twinx(ax)
ax.plot(df['B_ext_x'][:],df['<mx>'][:])
#ax.plot(df["#t"]*10**6,df['<mx>'],color='red',label='M')
#ax2.plot(df["#t"]*10**6,df['B_ext_x'],color='blue',label = 'B')
ax.set_xlabel('Applied field')
ax.set_ylabel('Magnetization')
ax2.set_ylabel('Applied field')
plt.legend()
plt.show()


#plt.figure()
#plt.hist(df['radius']*10**9,bins=150)
#plt.xlabel('radius [nm]')
#plt.ylabel('counts')
#plt.title('Size distribution of particles for simulation')
#plt.show()
