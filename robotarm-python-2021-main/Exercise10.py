from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
score = 10
for i in range (5):
    robotArm.grab()
    for i in range(1,score):
        robotArm.moveRight()
    robotArm.drop()
    score = score - 1
    for i in range(1,score):
        robotArm.moveLeft()
    score = score - 1
robotArm.wait()