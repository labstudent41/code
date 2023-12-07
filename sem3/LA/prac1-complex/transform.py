import matplotlib.pyplot as plt
s = [3+3j, 4+3j, 2+1j, 5+1j]
angle = int(input("Enter angle rotation from 90 or 180 degrees : "))

if angle == 90:
    s = [n * 1j for n in s]
elif angle == 180:
    s = [n * -1 for n in s]
else:
    print("Invalid Angle")

print(s)
x = [n.real for n in s]
y = [n.imag for n in s]
plt.plot(x, y, 'ro')
plt.axis([-6, 6, -6, 6])
plt.show()
