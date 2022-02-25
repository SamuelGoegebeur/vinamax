import numpy as np
import matplotlib.pyplot as plt

class cst:
    #No viscosity taken into account for the moment
    mu0 = 4*np.pi*1e-7          #m*kg/s**2/A**2
    G = 5/(4*np.pi*1e-7)        #A/m**2       
    A = 12e-3/(4*np.pi*1e-7)    #A/m
    omega0 = 2*np.pi*25e3       #Hz
    D = 30e-9                   #m
    Msat = 400e3                #A/m
    kB = 1.38064852e-23         #m**2*kg/s**2/K
    T = 310                     #K

def H(x,t):
    return cst.G*x-cst.A*np.cos(cst.omega0*t)   #A/m

def ksi(x,t):
    m =1/6*np.pi*cst.D**3*cst.Msat              #Am**2
    return cst.mu0*m/cst.kB/cst.T*H(x,t)        #/

def Langevin(x,t):
    return cst.Msat*(1/np.tanh(ksi(x,t))-1/ksi(x,t))    #A/m

def PSF(x,t):
    m =1/6*np.pi*cst.D**3*cst.Msat                  #Am**2
    PSF = cst.mu0*cst.Msat*m/cst.kB/cst.T*(-1/np.sinh(ksi(x,t))**2+1/ksi(x,t)**2)
    return PSF

def systemfunction(x,t):
    s = -cst.A*cst.omega0*np.sin(cst.omega0*t)*PSF(x,t)
    return s

def Kaczmarz(K,S,U):
    N,M  = np.shape(S)
    C = np.ones(M)
    for k in range(K):
        for j in range(N):
            C += (U[j]-np.matmul(S[j,:],C))*np.transpose(S[j,:])/np.matmul(S[j,:],np.transpose(S[j,:]))
            idx = np.where(C<0)[0]
            C[idx] = 0
    return C/np.max(C)