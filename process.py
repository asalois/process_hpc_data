import pandas as pd
#for i in range(1,11):
i = 1
print(str(i).zfill(2)+ " Samples")
print()
csv_name = "mse_" +str(i).zfill(2) + ".csv"
mse = pd.read_csv(csv_name,sep=' ',header=None)
mse.columns =["snr","MSE"]
frmt = ".7f"
test_sum = 0
for x in range(5,22):
    snr = mse[mse["snr"] == x]
    snr_test = snr.iloc[-1,1]
    test_sum += snr_test
    snr.drop(snr.tail(1).index)
    mean_cv = snr["MSE"].mean()
    diff = abs(snr_test - mean_cv)
    print("SNR =",x)
    print("CV mean MSE =",format(mean_cv,frmt))
    print("Test MSE    =",format(snr_test,frmt))
    print("Difference  =",format(diff,frmt))
    print()

print("Over all sum of test",format(test_sum,frmt))
