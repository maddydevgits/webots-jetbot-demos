from controller import Robot, Camera
import numpy as np
import cv2

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# === Camera ===
camera = robot.getDevice("camera")
camera.enable(timestep)
width = camera.getWidth()
height = camera.getHeight()

# === Motors ===
left_motor = robot.getDevice("left_wheel_hinge")
right_motor = robot.getDevice("right_wheel_hinge")
left_motor.setPosition(float('inf'))     # Velocity control mode
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# === Movement Functions ===
def stop():
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def forward(speed=3.0):
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

def backward(speed=3.0):
    left_motor.setVelocity(-speed)
    right_motor.setVelocity(-speed)

def turn_left(speed=3.0):
    left_motor.setVelocity(-speed)
    right_motor.setVelocity(speed)

def turn_right(speed=3.0):
    left_motor.setVelocity(speed)
    right_motor.setVelocity(-speed)

# === Main Loop ===
while robot.step(timestep) != -1:
    # Example: move forward, pause, then stop
    forward()
    robot.step(1000)  # move forward for ~1 second
    stop()
    robot.step(500)   # pause

    turn_left()
    robot.step(1000)
    stop()
    robot.step(500)

    turn_right()
    robot.step(1000)
    stop()
    robot.step(500)

    backward()
    robot.step(1000)
    stop()
    
