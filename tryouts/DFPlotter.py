import pandas as pd
import matplotlib.pyplot as plt

def plotter(df,x='#t'):
    df.plot(x=x)
    plt.show()