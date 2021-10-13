# Sort through hpc data in Python
import matplotlib.pyplot as plt
import scipy.io as spio
import math
import time
import numpy as np
import pandas as pd
start_time = time.time() # time it

matname = "data/noEqBER.mat"
mat = spio.loadmat(matname, squeeze_me=True)
ber = mat['BER']
data = []
data.extend(ber)
data.append(sum(ber))
data_add = np.array(data).reshape(1,32)
data1 = data_add

cols = []
snr = list(range(5,36))
cols.extend(snr)
cols.append('full sum')
df = pd.DataFrame(data1,columns=cols) # make df
df['k end sum'] = df.iloc[:,-(5+1):-1].sum(axis=1) # insert k end sum
df.to_pickle("no_eq.pkl") # save the meaningful data
print(df.shape)
print("--- %.2f seconds ---" % (time.time() - start_time))
