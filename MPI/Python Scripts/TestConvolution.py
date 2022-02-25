import numpy as np
from scipy.fftpack import fftfreq, fft
import matplotlib.pyplot as plt
from scipy.signal import convolve
from scipy import signal

t = np.arange(4000)*1e-8

omega = 2*np.pi*25e3
f = np.sin(omega*t)**2
#g = np.cos(omega*t)
g = np.repeat([0., 1.,1., 0.], 1000)
h = convolve(f,g,mode='same')/np.sum(g)
print(len(g))

#t = np.arange(300)
#f = np.repeat([0., 1., 0.], 100)
#g = signal.windows.hann(300)
#h =  signal.convolve(f, g, mode='same')/np.sum(g)


plt.figure()
plt.plot(t,f)
plt.plot(t,g)
plt.plot(t,h)
plt.show()

M = 30

N = len(t)
T = t[1]-t[0]
freq = fftfreq(N,T)[:N//2][:M]
F = 2/N*fft(f)[:N//2][:M]
G = 2/N*fft(g)[:N//2][:M]
H = 2/N*fft(h)[:N//2][:M]
print(freq)

plt.figure()
plt.scatter(freq,np.abs(F*G))
plt.scatter(freq,np.abs(H))
plt.show()
plt.figure()
#plt.scatter(freq,np.abs(F*G))
plt.scatter(freq,np.abs(H))
#plt.show()

