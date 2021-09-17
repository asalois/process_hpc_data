# Sort through hpc data in Python

import sys
import os
import scipy.io as spio
import math
import time
import numpy as np
import pandas as pd
start_time = time.time()

for i in range(1,990):
    # Load the data
    matname = "data/" + str(i).zfill(3) + "_ber_eqs.mat"
    try: 
        mat = spio.loadmat(matname, squeeze_me=True)
        ber = mat['ber']
        step = mat['step']
        trainNum = mat['trainNum']
        taps = mat['taps']
        data = [taps,step,trainNum]
        data.extend(ber)
        data.append(sum(ber))
        data_add = np.array(data).reshape(1,35)
        if i == 1:
            data1 = data_add
        else:
            data1 = np.concatenate((data1,data_add))
    except: # if no file
        #print(matname)
        pass

cols = ['taps','step','trainNum']
snr = list(range(1,32))
cols.extend(snr)
cols.append('sum')
df = pd.DataFrame(data1,columns=cols)
df = df.sort_values('sum')
df1 = df.head(20)
print(df)
print(df1)

print("--- %.2f seconds ---" % (time.time() - start_time))
