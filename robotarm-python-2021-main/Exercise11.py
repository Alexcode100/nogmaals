from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
for i in range(1,10):
    robotArm.moveRight()
for i in range(1,10):
    robotArm.grab()
    color = robotArm.scan()
    if color != "white":
        robotArm.drop()
        robotArm.moveLeft()
    elif color == "white":
        robotArm.moveRight()
        robotArm.drop()
        for i in range(1,3):
            robotArm.moveLeft()
robotArm.wait()