class Time:
  def __init__(self, hh, mm, ss):
    self.settime(hh, mm, ss)
  def settime(self, hh, mm, ss):
    self.hh = hh
    self.mm = mm
    self.ss = ss
  def showtime(self):
    print("%02d:%02d:%02d" % (self.hh, self.mm, self.ss))
  def addtime(self, t2):
    self.hh += t2.hh
    self.mm += t2.mm
    self.ss += t2.ss
    if self.ss > 60:
      self.ss %= 60
      self.mm += 1
    if self.mm > 60:
      self.mm %= 60
      self.hh += 1

t1 = Time(11, 48, 40)
t1.showtime()

t2 = Time(11, 50, 30)
t2.showtime()

t1.addtime(t2)
t1.showtime()
