import os


def lcs(a, b):

    def display():
        row = len(L)
        col = len(L[0])
        print('\n')

        # print table heading (indexes of columns)
        print('\t', end='')  # give some gap for heading
        for i in range(col):
            print("%s\t" % i, end='')

        # print a line
        print("\n      +", end='')
        print("-"*(col*8), end='')

        # print table data
        for i in range(row):
            print("\n %4s |\t" %i, end='')
            for j in range(col):
                print("%s\t" %L[i][j], end='')

        print('\n\n')


    m = len(a)
    n = len(b)
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            os.system('clear')
            print("a: %s\tb : %s" %(a, b))
            print("i, j :  %d, %d\n" %(i, j))

            if i==0 or j==0:
                print("Setting L[{}][{}] to 0".format(i, j))
                print()
                print()
                L[i][j] = 0
            else:
                print("Comparing \ta[i-1] \tb[j-1]")
                print("          \ta[{}] \tb[{}]".format(i-1, j-1))
                print("          \t{}     \t{}    ".format(a[i-1], b[j-1]))
                if a[i-1] == b[j-1]:
                    print("Matched!")
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])

            display()
            input("Press Enter to continue ")

    return L[m][n]


#main
s1 = "AGGTAB"
s2 = "GXTXAYB"
print("The length of Longest common subsequence is", lcs(s1, s2))

