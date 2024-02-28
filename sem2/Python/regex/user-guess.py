class ValueTooSmall(Exception):
    def display(self):
        print("Input value smaller than range")

class ValueTooLarge(Exception):
    def display(self):
        print("Input greater than range")

try:
    num = int(input("Input a number between 1 to 100 : "))
    if num < 0:
        raise ValueTooSmall
    elif num > 100:
        raise ValueTooLarge
    else:
        print(num, "was entered")
except (ValueTooLarge, ValueTooSmall) as e:
    e.display()
