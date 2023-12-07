processes = 5
resources = 3
max_resources = [10, 5, 7]

currently_allocated = [[0, 1, 0],
                       [2, 0, 0],
                       [3, 0, 2],
                       [2, 1, 1],
                       [0, 0, 2]]

max_need = [[7, 4, 3],
            [1, 2, 2],
            [6, 0, 0],
            [0, 1, 1],
            [4, 3, 1]]

#    processes = int(input("Enter no. of processes : "))
#    resources = int(input("Enter no. of resources : "))
#    max_resources = [int(i) for i in input("Max resource : ").split()]

#    print("\nAllocated resources for each process")
#    currently_allocated = [[int(i)
#            for i in input("process %d : " % (j+1)).split(' ')]
#               for j in range(processes)]

#    print("\nMaximum resources needed for each process")
#    max_need = [[int(i)
#            for i in input("process %s : " %(j+1)).split()]
#                for j in range(processes)]

allocated = [0] * resources
for i in range(processes):
    for j in range(resources):
        allocated[j] += currently_allocated[i][j]

print("\nTotal allocated resources : %s\n" % (allocated))
available = [max_resources[i] - allocated[i] for i in range(resources)]

print("\nTotal available resources : %s\n" % (available))
running = [True] * processes
count = processes
while count != 0:
    safe = False
    for i in range(processes):
        if running[i]:
            executing = True
            for j in range(resources):
                if max_need[i][j] - currently_allocated[i][j] > available[j]:
                    executing = False
                    break

            if executing:
                print("\nProcess%s is executing" % (i+1))
                running[i] = False
                count -= 1
                safe = True
                for j in range(resources):
                    available[j] += currently_allocated[i][j]
                break

    if not safe:
        print("Processes are in an unsafe state")
        break
    print("The process is in a safe state")
    print("Available resource : ", available)
