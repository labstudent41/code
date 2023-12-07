import matplotlib.pyplot as plt

def complex_plot(nums):
    print(nums)
    x = [num.real for num in nums]
    y = [num.imag for num in nums]
    plt.xlabel('Real')
    plt.ylabel('Imaginary ')
    plt.axis([-6, 6, -6, 6])
    plt.plot(x, y, 'g*')
    plt.show()

S = [3+3j, 4+3j, 2+1j, 5+1j]
complex_plot(S)

s = [x*1j for x in S]
complex_plot(s)

s = [x*-1 for x in S]
complex_plot(s)

