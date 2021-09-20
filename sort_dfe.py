# Sort through hpc data in Python
import matplotlib.pyplot as plt
import scipy.io as spio
import math
import time
import numpy as np
import pandas as pd
start_time = time.time()

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
        data_add = np.array(data).reshape(1,35)
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
df = pd.DataFrame(data1,columns=cols)
df = df.sort_values('full sum')
df = df.drop_duplicates(subset=['taps','ftaps','trainNum'])
df = df[df['full sum'] < 31]
df = df[df['taps'] > df['ftaps']]
df['k end sum'] = df.iloc[:,-(5+1):-1].sum(axis=1)
for k in range(5,31,5):
    df['k end sum'] = df.iloc[:,-(k+1):-2].sum(axis=1)
    df = df.sort_values('k end sum')
    df1 = df.head(5)
    df_ber = df1.iloc[:,3:34].copy().T
    ber_cols = list()
    for index, row in df1.iterrows():
        ber_cols.append(\
                "tps={a:d} ftps={b:d} trn={c:d}"\
                .format(a=int(row['taps']), b=int(row['ftaps']), c=int(math.log2(row['trainNum']))))
    df_ber.columns = ber_cols
    print(df1)
    df_ber.plot(style='x-',kind='line',logy=False,\
            title="DFE Scan Ber",xlabel="SNR dB",ylabel="BER")
    fig_name = "dfe_k_%d.png" % k
    plt.savefig(fig_name)
print(df.shape)
print("--- %.2f seconds ---" % (time.time() - start_time))
