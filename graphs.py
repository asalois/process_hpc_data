# Sort through hpc data in Python
import matplotlib.pyplot as plt
import math
import time
import numpy as np
import pandas as pd
start_time = time.time()

df_dfe = pd.read_pickle("dfe.pkl")
df_lms = pd.read_pickle("lms.pkl")
df_ann = pd.read_pickle("ann.pkl")

for k in range(5,31,5):
    df_lms['k end sum'] = df_lms.iloc[:,-(k+1):-2].sum(axis=1)
    df_lms = df_lms.sort_values('k end sum')
    df = df_lms.head(5)
    df_ber = df.iloc[:,3:34].copy().T
    ber_cols = list()
    for index, row in df.iterrows():
        ber_cols.append(\
            "tps={0:d} stp={1:1.3f} trn={2:d}"\
            .format(int(row['taps']), row['step'], int(math.log2(row['trainNum']))))
    df_ber.columns = ber_cols
    df_ber.plot(style='x-',kind='line',logy=True,\
            title="LMS Scan Ber",xlabel="SNR dB",ylabel="BER")
    fig_name = "lms_k_%d.png" % k
    plt.savefig(fig_name)
    plt.close()

for k in range(5,31,5):
    df_dfe['k end sum'] = df_dfe.iloc[:,-(k+1):-2].sum(axis=1)
    df_dfe = df_dfe.sort_values('k end sum')
    df = df_dfe.head(5)
    df_ber = df.iloc[:,3:34].copy().T
    ber_cols = list()
    for index, row in df.iterrows():
        ber_cols.append(\
            "tps={0:d} ftps={1:d} trn={2:d}"\
            .format(int(row['taps']), int(row['ftaps']), int(math.log2(row['trainNum']))))
    df_ber.columns = ber_cols
    df_ber.plot(style='x-',kind='line',logy=False,\
            title="DFE Scan Ber",xlabel="SNR dB",ylabel="BER")
    fig_name = "dfe_k_%d.png" % k
    plt.savefig(fig_name)
    plt.close()

for k in range(5,31,5):
    df_ann['k end sum'] = df_ann.iloc[:,-(k+1):-2].sum(axis=1)
    df_ann = df_ann.sort_values('k end sum')
    df = df_ann.head(5)
    df_ber = df.iloc[:,2:-2].copy().T
    ber_cols = list()
    for index, row in df.iterrows():
        ber_cols.append(\
            "{0} smpl={1:d}"\
            .format(row['arch'],row['samples']))
    df_ber.columns = ber_cols
    df_ber.plot(style='x-',kind='line',logy=True,\
            title="ANN Ber",xlabel="SNR dB",ylabel="BER")
    fig_name = "ann_k_%d.png" % k
    plt.savefig(fig_name)
    plt.close()

df = df_ann.sort_values('full sum')
df = df.drop_duplicates(subset=['arch'])
df_ber = df.iloc[:,2:-2].copy().T
ber_cols = list()
for index, row in df.iterrows():
    ber_cols.append(\
        "{0} smpl={1:d}"\
        .format(row['arch'],row['samples']))
df_ber.columns = ber_cols
df_ber.plot(style='x-',kind='line',logy=True,\
        title="Best per Arch",xlabel="SNR dB",ylabel="BER")
fig_name = "ann_archs.png"
plt.savefig(fig_name)
plt.close()


for k in range(1,11):
    df = df_ann[ df_ann['samples'] == k]
    df_ber = df.iloc[:,2:-2].copy().T
    ber_cols = list()
    for index, row in df.iterrows():
        ber_cols.append(\
            "{0}"\
            .format(row['arch']))
    df_ber.columns = ber_cols
    fig_title = "%d samples" % k
    df_ber.plot(style='x-',kind='line',logy=True,\
            title=fig_title,xlabel="SNR dB",ylabel="BER")
    fig_name = "ann_samples_%d.png" % k
    plt.savefig(fig_name)
    plt.close()

df_ann = df_ann.sort_values('samples')
for arch in df_ann['arch']:
    df = df_ann[ df_ann['arch'] == arch]
    df_ber = df.iloc[:,2:-2].copy().T
    ber_cols = list()
    for index, row in df.iterrows():
        ber_cols.append(\
            "smpl={0:d}"\
            .format(row['samples']))
    df_ber.columns = ber_cols
    fig_title = "%s" % arch.replace("_"," ")
    df_ber.plot(style='x-',kind='line',logy=True,\
            title=fig_title,xlabel="SNR dB",ylabel="BER")
    fig_name = "ann_arch_%s.png" % arch
    plt.savefig(fig_name)
    plt.close()

print("--- %.2f seconds ---" % (time.time() - start_time))
