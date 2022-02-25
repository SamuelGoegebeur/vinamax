directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\1D.out\\'
file = 'MNPs101_radius30_x-2.240mm.txt'


df = DataReader.get_all_data(directory+file,printtf=False)

def plot(df,loc = [0.2,-0.2]):
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    #ax3 = fig.add_subplot(313)
    ax.plot(df['#t']*10**6,df['B_x@('+str(loc[0])+',0,0)'])
    ax2.plot(df['#t']*10**6,df['B_x@('+str(loc[1])+',0,0)'])
    #ax3.plot(df['#t']*10**6,df['B_x@('+str(loc[2])+',0,0)'])
    ax.set_xticklabels([])
    #ax2.set_xticklabels([])
    ax.set_ylabel('@{}'.format(loc[0]))
    ax2.set_ylabel('@{}'.format(loc[1]))
    #ax3.set_ylabel('@{:.0e}'.format(loc[2]))
    ax2.set_xlabel('Time [µs]')
    print(len(df['#t']))
    
    plt.show()

plot(df, loc = [0.2,-0.2])