# Sort through hpc data in Python
import matplotlib.pyplot as plt
import scipy.io as spio
import math
import time
import numpy as np
import pandas as pd
start_time = time.time()
k = 10

for i in range(1,3543): # load in data
    matname = "data/dfe/" + str(i).zfill(4) + "_ber_eqs.mat"
    try: 
        mat = spio.loadmat(matname, squeeze_me=True)
        ber = mat['ber']
        trainNum = mat['trainNum']
        taps = mat['taps']
        ftaps = mat['ftaps']
        data = [taps,ftaps,trainNum]
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

cols = ['taps','ftaps','trainNum']
snr = list(range(5,36))
cols.extend(snr)
cols.append('full sum')
cols.append('k end sum')
df = pd.DataFrame(data1,columns=cols)
df = df.sort_values('k end sum')
df = df.drop_duplicates(subset=['taps','ftaps','trainNum'])
df1 = df.head(5)
df_ber = df1.iloc[:,3:34].copy().T
ber_cols = list()
for index, row in df1.iterrows():
    ber_cols.append(\
            "tps={a:d} ftps={b:d} trn={c:d}"\
            .format(a=int(row['taps']), b=int(row['ftaps']), c=int(math.log2(row['trainNum']))))
df_ber.columns = ber_cols
print(df)
print(df1)
print(df_ber)
df_ber.plot(style='x-',kind='line',logy=False,\
        title="LMS Scan Ber",xlabel="SNR dB",ylabel="BER")
plt.show()
print("--- %.2f seconds ---" % (time.time() - start_time))
