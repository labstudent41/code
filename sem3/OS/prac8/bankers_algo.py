nProcs = 5  # no. of processess
nResources = 3  # no. of resourcess
max_resources = [10, 5, 7]  # available in the system

# for each process
allocated = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]
max_need = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [4, 2, 2],
    [5, 3, 3],
]

total_allocated = [0] * nResources
remaining_need = [[0] * nResources for _ in range(nProcs)]
for i in range(nProcs):
    for j in range(nResources):
        total_allocated[j] += allocated[i][j]
        remaining_need[i][j] = max_need[i][j] - allocated[i][j]

available = [[0] * nResources for _ in range(nProcs+1)]
for i in range(nResources):
    available[0][i] = max_resources[i] - total_allocated[i]

print("\nAvailable Resources :  %s\n" % available[0])

count = 0  # finished processess
waiting = [True] * nProcs
state = ['Undetermined'] * nProcs
order = [0] * nProcs
while count < nProcs:
    previous_count = count
    for i in range(nProcs):
        if not waiting[i]:
            continue
        running = True
        for j in range(nResources):
            difference = available[count][j] - remaining_need[i][j]
            if difference < 0:
                running = False
                break
            available[count+1][j] = available[count][j] + allocated[i][j]
        if running:
            print("\n> Executing process", i)
            print("  Available Resources : ", available[count+1])
            waiting[i] = False
            state[i] = 'Safe'
            count += 1
    if previous_count == count:
        print("\n!!! Deadlock Occured !!!")
        break


# Printing final table
line_format = "%-8s %-12s %-12s %-12s %-8s"
print('\n')
print('-' * 60)
print(line_format %
      ("Process", "Allocated", "Max", "Remaining", "State"))
print(line_format % ("", "", "Need", "Need", ""))
print('-' * 60)
for i in range(nProcs):
    print(line_format % ('P'+str(i+1), allocated[i], max_need[i],
                         remaining_need[i], state[i]))
