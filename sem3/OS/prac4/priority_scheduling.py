def sort_procs(n, bt, p):  # sort processes by priorities in place
    for i in range(n):
        x = i
        for j in range(i, n):
            if p[j] < p[x]:
                x = j
        if x != i:
            p[i], p[x] = p[x], p[i]
            bt[i], bt[x] = bt[x], bt[i]

# bt = [10, 8, 12, 6]
bt = [6, 9, 7, 4]
p = [3, 2, 1, 4]
n = len(bt)

sort_procs(n, bt, p)
wt, tat = [0], [bt[0]]
for i in range(1, n):
    wt.insert(i, wt[i-1] + bt[i-1])
    tat.insert(i, wt[i] + bt[i])

line_format = "%8s %8s %4s %4s %4s"
print(line_format % ("Process", "Priority", "BT", "WT", "TAT"))
for i in range(n):
    print(line_format % (i+1, p[i], bt[i], wt[i], tat[i]))

print("Avg waiting time : ", sum(wt)/n)
print("Avg turnaround time : ", sum(tat)/n)
