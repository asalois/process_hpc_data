# Sort through hpc data in Python
import matplotlib.pyplot as plt
import scipy.io as spio
import math
import time
import numpy as np
import pandas as pd
start_time = time.time()
k = 10

for i in range(1,990): # load in data
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
        data.append(sum(ber[-k:]))
        data_add = np.array(data).reshape(1,36)
        data_add_ber = np.array(ber).reshape(31,1)
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
cols.append('k end sum')
df = pd.DataFrame(data1,columns=cols)
df = df.sort_values('k end sum')
df1 = df.head(5)
df_ber = df1.iloc[:,3:34].copy().T
ber_cols = list()
for index, row in df1.iterrows():
    ber_cols.append(\
            "tps={a:d} stp={b:1.2f} trn={c:d}"\
            .format(a=int(row['taps']), b=row['step'], c=int(math.log2(row['trainNum']))))
df_ber.columns = ber_cols
#print(df)
print(df1)
print(df_ber)
df_ber.plot(style='x-',kind='line',logy=True,\
        title="LMS Scan Ber",xlabel="SNR dB",ylabel="BER")
plt.show()
print("--- %.2f seconds ---" % (time.time() - start_time))
