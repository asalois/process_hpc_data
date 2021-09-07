import pandas as pd
sums = []
names = []
for i in range(1,11):
    name = str(i).zfill(2) + " Samples"
    names.append(name)
    print(str(i).zfill(2)+ " Samples")
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
        if diff > 0.01:
            print("SNR =",x)
            print("CV mean MSE =",format(mean_cv,frmt))
            print("Test MSE    =",format(snr_test,frmt))
            print("Difference  =",format(diff,frmt),"\n")
    sums.append(test_sum)
    print("Over all sum of test",format(test_sum,frmt),"\n")

min_sum = min(sums)
print(names[sums.index(min(sums))],"has the min at",min_sum)

