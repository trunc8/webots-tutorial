"""four_wheeled_collision_avoidance controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
MAX_SPEED = 1.0

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot.
ds = []
dsNames = ['ds_left', 'ds_right']
for i in range(2):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(timestep)

wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

avoidObstacleCounter = 0
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    leftSpeed = MAX_SPEED
    rightSpeed = MAX_SPEED
    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        leftSpeed = MAX_SPEED
        rightSpeed = -MAX_SPEED
    else:
        for i in range(2):
            if ds[i].getValue() < 950:
                avoidObstacleCounter = 100
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    

    # Process sensor data here.

    
    wheels[0].setVelocity(leftSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[3].setVelocity(rightSpeed)

# Enter here exit cleanup code.
