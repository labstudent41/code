import timeit

def TowerOfHanoi(n, src, dest, temp):
    if n == 1:
        print("Move disk from source %s to destination %s" %
              (src, dest))
        return
    TowerOfHanoi(n-1, src, temp, dest)
    print("Move disk from source %s to destination %s" %
              (src, dest))
    TowerOfHanoi(n-1, temp, dest, src)

n = int(input("Enter number of discs : "))
TowerOfHanoi(n, 'A', 'B', 'C')
print("Finished in %fs" % timeit.timeit())
