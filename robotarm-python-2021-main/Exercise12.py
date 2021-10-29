from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
for i in range(1,100):
    robotArm.grab()
    color = robotArm.scan()
    if color != "red":
        robotArm.drop()
        robotArm.moveRight()
    elif color == "red":
        for i in range(1,10):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(1,10):
            robotArm.moveLeft()
robotArm.wait()