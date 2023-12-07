class Date:

    def __init__(self, dd, mm, yy):
        self.getdata(dd, mm, yy)

    def getdata(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def show(self):
        print("%s/%s/%s" % (self.dd, self.mm, self.yy))

    def isNewYear(self):
        return self.dd == 1 and self.mm == 1

    def isLeapYear(self):
        return self.yy % 4 == 0 and (
                self.yy % 100 != 0 or self.yy % 400 == 0)

    def isIndependenceDay(self):
        return self.dd == 15 and self.mm == 8

    def day_after_week(self):
        self.dd += 7
        if self.dd > 30:
            self.dd %= 30
            self.mm += 1
        if self.yy > 12:
            self.mm = self.mm % 12
            self.mm += 1


today = Date(26, 6, 2023)
print("Todays date :-")
today.show()
today.day_after_week()
print("Date after a week :-")
today.show()

print()
aug15 = Date(15, 8, 2020)
if aug15.isIndependenceDay():
    print("Happy Independence Day")

jan1 = Date(1, 1, 2020)
if jan1.isNewYear():
    print("Happy New Year 2020")
if jan1.isLeapYear():
    print("This is leap year")
