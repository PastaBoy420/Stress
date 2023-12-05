import numpy as np
import pandas as pd
import mne

path = 'C:\\Users\maste\Documents\Python'
data = pd.read_csv(path + '\Filter-1-35-Hz-Spliced-S4-2nd.csv',
            skiprows=0,usecols=[*range(0, 16)])
ch_names = ['FP1', 'FP2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2', 'F7',
            'F8', 'F3', 'F4', 'T7', 'T8', 'P3', 'P4']
data2 = data.transpose()
sfreq = 125
info = mne.create_info(ch_names=ch_names, sfreq=sfreq)
raw = mne.io.RawArray(data2, info)
raw.plot()
raw.save('Filter-1-35-Hz-Spliced-S4-2nd-raw.fif')