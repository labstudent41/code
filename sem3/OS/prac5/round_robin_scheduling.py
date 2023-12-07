def getTAT(n, bt, at, time_slice):
    rt = bt.copy() # remaining time
    tat = [0] * n  # turn around times
    ready = []     # ready queue
    i = 0  # process counter for incoming processess
    currtime = 0

    while i < n or ready:
        if len(ready) == 0:
            currtime += at[i]
            ready.append(i)
            i += 1

        p = ready[0]
        # print("%2s %2s %-15s %-15s" % (p, currtime, rt, ready))
        if rt[p] > time_slice:
            currtime += time_slice
            rt[p] -= time_slice
        else:
            currtime += rt[p]
            rt[p] -= rt[p]
            tat[p] = currtime - at[p]

        while i < n and at[i] <= currtime:
            ready.append(i)
            i += 1

        ready.pop(0)
        if rt[p]:
            ready.append(p)

    return tat


def getWT(n, bt, tat):
    wt = [0] * n
    for i in range(n):
        wt[i] = tat[i] - bt[i]
    return wt

bt = [5, 3, 1, 2, 3]
at = [0, 1, 2, 3, 4]
n = len(bt)

tat = getTAT(n, bt, at, 2)
wt = getWT(n, bt, tat)

line_format = "%8s  %4s %4s %4s"
print(line_format % ("Process", "BT", "WT", "TAT"))
for i in range(n):
    print(line_format % (i+1, bt[i], wt[i], tat[i]))

print("Avg waiting time = ", sum(wt)/n)
print("Avg turn around time = ", sum(tat)/n)
