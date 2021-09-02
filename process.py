import pandas as pd
mse = pd.read_csv('mses.csv',sep=' ',header=None)
mse.columns =["snr","MSE"]
frmt = ".6f"
for x in range(5,22):
    snr = mse[mse["snr"] == x]
    snrtest = snr.iloc[-1,1]
    snr.drop(snr.tail(1).index)
    print("SNR =",x)
    print("CV mean MSE =",format(snr["MSE"].mean(),frmt))
    print("Test MSE    =",format(snrtest,frmt))
    print()
