import statistics

data_A = [10,11,14,20,20,20,22,24,28,31]
data_B = [2,9,13,14,20,20,24,26,32,40]

mean_A = statistics.mean(data_A)
median_A = statistics.median(data_A)
mode_A = statistics.mode(data_A)
vari_A = statistics.variance(data_A)

mean_B = statistics.mean(data_B)
median_B = statistics.median(data_B)
mode_B = statistics.mode(data_B)
vari_B = statistics.variance(data_B)

print ("Data A Mean =", mean_A)
print ("Data A Median =", median_A)
print ("Data A Mode=", mode_A)
print ("Data A Variance =", vari_A)

print ("Data B Mean =", mean_B)
print ("Data B Median =", median_B)
print ("Data B Mode =", mode_B)
print ("Data B Vairance =", vari_B)