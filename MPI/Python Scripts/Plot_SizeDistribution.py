from numpy.core.fromnumeric import searchsorted
import pandas as pd
import matplotlib.pyplot as plt
params = {
    #'text.usetex' : True,
    'font.size' : 18,
    'font.serif' :'cm',
    #'text.latex.unicode': True
}


directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\'
file = 'PaperParticles\\Hysteresis.out\\geometry000000.txt'


def get_all_data(file,delimiter='\s+',skiprows=0,printtf=False):
    data = pd.read_csv(file,delimiter=delimiter,skiprows=skiprows)
    df = pd.DataFrame(data)
    if printtf:
        print(df)
    return df

def plot_size(df):
    plt.figure()
    plt.hist(df['radius']*10**9,bins=150)
    plt.xlabel('radius [nm]')
    plt.ylabel('counts')
    plt.title('Size distribution of particles for simulation')
    plt.show()

df = get_all_data(directory+file)
plot_size(df)
