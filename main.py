import random


class Warrior:
  def __init__(self,health):
    self.health = health

  def hit(self,target,target1):
    if target.health > 0:
      target.health -= 20
      if target1 == warrior1:
        target1 = "Воин1"
      if target1 == warrior2:
        target1 = "Воин2"
      print(target1, " Атакует")
      print(target.health/20, "УДАРОВ ДО ПОБЕДЫ")
    if target.health == 0:
      print(target1, " Победитель \n GAME OVER")


warrior1 = Warrior(100)
warrior2 = Warrior(100)


q = int(input("Нажмите 1 чтобы ударить, 2 чтобы остановить бой"))

while q != 2:
  if q == 1:
    j = random.randint(1,3)
    if j % 2 == 0:
      warrior1.hit(warrior2,warrior1)
      q = int(input("Нажмите 1 чтобы ударить:"))
    else:
      warrior2.hit(warrior1,warrior2)
      q = int(input("Нажмите 1 чтобы ударить:"))
  else:
    print("=)")
    break