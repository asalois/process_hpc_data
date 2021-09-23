# Sort through hpc data in Python
import matplotlib.pyplot as plt
import scipy.io as spio
import math
import time
import numpy as np
import pandas as pd
start_time = time.time()

archs = [
"e10_12linear",
"e10_12relu_12tanh_12tanh_12tanh_12tanh_12tanh",
"e10_12relu_12tanh_8tanh_4tanh_8tanh_12tanh",
"e10_12relu_12tanh",
"e10_12relu_4tanh_6tanh_8tanh_10tanh_12tanh",
"e10_12tanh_12relu"
]

for i, arch in enumerate(archs): # load in data
    matname = "data/ann/" + arch + "_berDNNTF.mat"
    mat = spio.loadmat(matname, squeeze_me=True)
    ber = mat['ber']
    data = ber
    sums = np.sum((ber), axis=1).reshape((10,1))
    data_add = np.hstack((ber,sums))
    cols = list(range(5,36))
    cols.append("full sum")
    df1 = pd.DataFrame(data_add,columns=cols)
    df1.insert(0,'arch',arch[4:])
    df1.insert(1,'samples', df1.index + 1)
    if i == 0:
        df_all = df1
    else:
        df_all = df_all.append(df1,ignore_index=True)

df_all['k end sum'] = df_all.iloc[:,-(10+1):-1].sum(axis=1)
df_all = df_all.sort_values('full sum')
df_all.to_pickle("ann.pkl")
print(df_all.shape)
print("--- %.2f seconds ---" % (time.time() - start_time))
