import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.fftpack import fft, fftfreq, ifft
"""

t = np.linspace(0,25,1000)
l = np.sin(2*np.pi/5*t)+np.cos(2*np.pi/6*t)

N = len(t)
T = t[1]-t[0]
freq = fftfreq(N, T)[:N//2][0:30]
spectrum = 2/N*fft(l)[:N//2][:30]

l_new =0    
for i in range(len(spectrum)):
    l_new += spectrum[i]*np.exp(2j*np.pi*t*freq[i])
 
plt.figure()
plt.plot(t,np.real(l_new),label='real')
plt.plot(t,np.imag(l_new),label='imag')
#plt.plot(t,np.abs(l_new),label='abs')
plt.plot(t,l,label='orig')
plt.legend()
plt.show()
"""

from scipy import signal
sig = np.repeat([0., 1., 0.], 100)
win = signal.windows.hann(50)
c =  signal.convolve(sig, win, mode='same')
filtered = signal.convolve(sig, win, mode='same') / sum(win)
print(len(sig))
print(len(win))
print(len(c))
print(len(filtered))