import numpy as np
import pandas as pd

import Xspace

def create_dataframes(N,M,x,t,directory):
    S = np.zeros((N,M))
    H_ap = np.zeros((N,M))
    xi = np.zeros((N,M))
    P = np.zeros((N,M))

    for i,xi in enumerate(x):
        for j,tj in enumerate(t):
            S[j,i] = Xspace.systemfunction(xi,tj)
            H_ap[j,i] = Xspace.H(xi,tj)
            xi[j,i] = Xspace.ksi(xi,tj)
            P[j,i] = Xspace.PSF(xi,tj)


    df_S = pd.DataFrame(S,columns=x*1e3,index=t*1e6)
    df_H = pd.DataFrame(H_ap,columns=x*1e3,index=t*1e6)
    df_ksi = pd.DataFrame(xi,columns=x*1e3,index=t*1e6)
    df_PSF = pd.DataFrame(P,columns=x*1e3,index=t*1e6)

    df_S.to_csv(directory+'S.txt',sep='\t')
    df_H.to_csv(directory+'H.txt',sep='\t')
    df_ksi.to_csv(directory+'Ksi.txt',sep='\t')
    df_PSF.to_csv(directory+'PSF.txt',sep='\t')


