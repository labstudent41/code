# n = int(input("Enter the no. of processess : "))
# plist = input("Enter the burst time of process : ")
# plist = "2 3 9 1 5 6 3"
plist = "10 8 12 6"
bt = sorted(list(map(int, plist.split())))
n = len(bt)

avgwt, avgtat = 0, bt[0]
wt, tat = [0], [bt[0]]

for i in range(1, n):
    wt.insert(i, wt[i-1] + bt[i-1])
    tat.insert(i, wt[i] + bt[i])
    avgwt += wt[i]
    avgtat += tat[i]

avgwt /= n
avgtat /= n

line_format = '+' + '-'*14 + '+' + '-'*14 + '+' + '-'*16 + '+' + '-'*20 + '+'
print("No. of processess : ", n)
print(line_format)
print("| %-12s | %-12s | %-14s | %-18s |" %
      ("Process", "Burst time", "Waiting time",
       "Turn around time"))
print(line_format)
for i in range(n):
    print("| %-12d | %-12d | %-14d | %-18d |" %
          (i+1, bt[i], wt[i], tat[i]))
print(line_format)
print("Avg waiting time = ", avgwt)
print("Avg turnaround time = ", avgtat)
