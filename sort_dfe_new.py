# Sort through hpc data in Python
import matplotlib.pyplot as plt
import scipy.io as spio
import math
import time
import numpy as np
import pandas as pd
start_time = time.time()

for i in range(1,64601): # load in data
    matname = "data/dfe_new/" + str(i).zfill(5) + "_ber_eqs.mat"
    try: 
        mat = spio.loadmat(matname, squeeze_me=True)
        ber = mat['ber']
        trainNum = mat['trainNum']
        taps = mat['taps']
        ftaps = mat['ftaps']
        step = mat['step']
        data = [taps,ftaps,step,trainNum]
        data.extend(ber)
        data.append(sum(ber))
        data_add = np.array(data).reshape(1,36)
        data_add_ber = np.array(ber).reshape(31,1)
        if i == 1:
            data1 = data_add
        else:
            data1 = np.concatenate((data1,data_add))
    except: # if no file
        # do nothing
        pass

cols = ['taps','ftaps','step','trainNum']
snr = list(range(5,36))
cols.extend(snr)
cols.append('full sum')
df = pd.DataFrame(data1,columns=cols)
df = df.sort_values('full sum')
df_all = df.sort_values('full sum')
df = df.drop_duplicates(subset=['taps','ftaps','trainNum','step'])
df = df[df['full sum'] < 16]
df = df[df['taps'] > df['ftaps']]
df['k end sum'] = df.iloc[:,-(5+1):-1].sum(axis=1)
df.to_pickle("dfe_new.pkl")
df_all.to_pickle("dfe_new_all.pkl")
print(df.head(5))
print(df.shape)
print("--- %.2f seconds ---" % (time.time() - start_time))
