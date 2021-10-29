from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
times = 1
for i in range(1,8):
    robotArm.grab()
    color = robotArm.scan()
    if color =='':
        break
    else:
        for i in range(times):
            robotArm.moveRight()
        robotArm.drop()
        times = times + 1
        for i in range(times):    
            robotArm.moveLeft()
robotArm.wait()