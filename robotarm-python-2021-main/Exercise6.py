#Alexander den Otter  -  9067410
#Oefening 6
from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 2

for i in range(1,8):
    robotArm.moveRight()

for i in range(1,9):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()