from controller import Robot, Camera
import numpy as np
import cv2

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Enable JetBot camera
camera = robot.getDevice("camera")
camera.enable(timestep)
width = camera.getWidth()
height = camera.getHeight()

while robot.step(timestep) != -1:
    # Get camera image from Webots
    image = camera.getImage()

    # Convert to OpenCV format (BGRA to BGR)
    img = np.frombuffer(image, dtype=np.uint8).reshape((height, width, 4))
    frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # === Yellow Color Range ===
    # Updated tighter yellow range
    lower_yellow = np.array([25, 150, 150])
    upper_yellow = np.array([32, 255, 255])
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    yellow_pixels = cv2.countNonZero(mask_yellow)


    # === Red Color Range ===
    # Red appears in 2 HSV ranges due to circular hue
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    red_pixels = cv2.countNonZero(mask_red)

    # === Print detections ===
    print("🟡 Yellow pixels:", yellow_pixels)
    print("🔴 Red pixels:", red_pixels)

    if yellow_pixels > 200:
        print("✅ Yellow color detected!")

    if red_pixels > 200:
        print("✅ Red color detected!")

    # Optional: save snapshots for debugging
    # cv2.imwrite("frame.jpg", frame)
    # cv2.imwrite("yellow_mask.jpg", mask_yellow)
    # cv2.imwrite("red_mask.jpg", mask_red)
