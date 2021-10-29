from RobotArm import RobotArm ; robotArm = RobotArm('exercise 9')
for i in range(4):
    for i in range(4):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(4):
            robotArm.moveLeft()
    for i in range(4):
        robotArm.moveLeft()
robotArm.wait()
