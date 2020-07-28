"""epuck_go_forward controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

TIMESTEP = 64
MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# get the motor devices
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')

# set the target position of the motors to infinity (speed control)
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# set up the motor speeds at 10% of the MAX_SPEED.
leftMotor.setVelocity(0.1 * MAX_SPEED)
rightMotor.setVelocity(0.1 * MAX_SPEED)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIMESTEP) != -1:
    pass

# Enter here exit cleanup code.
