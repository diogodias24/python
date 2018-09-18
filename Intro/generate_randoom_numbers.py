import random

potion_health = random.randint(25, 50)

health = 50

dificulty = random.randint(1,3)

health = int(health + potion_health / dificulty)

print(health)
  
