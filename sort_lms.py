# Sort through hpc data in Python
import matplotlib.pyplot as plt
import scipy.io as spio
import math
import time
import numpy as np
import pandas as pd
start_time = time.time() # time it

for i in range(1,2000): # load in data
    matname = "data/lms/" + str(i).zfill(3) + "_ber_eqs.mat"
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
        # do nothing
        pass

cols = ['taps','step','trainNum']
snr = list(range(5,36))
cols.extend(snr)
cols.append('full sum')
df = pd.DataFrame(data1,columns=cols) # make df
df_all = df.copy() # copy all data 
df = df[df['full sum'] < 16] # rid of all sums over 16
df['k end sum'] = df.iloc[:,-(5+1):-1].sum(axis=1) # insert k end sum
df.to_pickle("lms.pkl") # save the meaningful data
df_all.to_pickle("lms_all.pkl") # save all the data
print(df.shape)
print("--- %.2f seconds ---" % (time.time() - start_time))
