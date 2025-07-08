
# 🤖 JetBot Color Detection and Movement in Webots

This project simulates an **NVIDIA JetBot** in Webots that detects **yellow** and **red colors** using its camera and responds with corresponding **movements**. The controller is written in Python and uses **OpenCV** for image processing.

---

## 🚀 Features

- ✅ Real-time color detection using the robot's camera
- 🎨 HSV-based masking with OpenCV for accurate red/yellow identification
- 🧠 Motor control functions: move forward, backward, turn, and stop
- 📦 Lightweight, Python-only implementation—no C compilation required

---

## 📂 Project Structure

```
jetbot-color-detection/
├── controllers/
│   └── jetbot_color_detect/
│       └── jetbot_color_detect.py
├── worlds/
│   └── jetbot.wbt
├── README.md
```

---

## 📦 Requirements

- [Webots](https://cyberbotics.com/) (2023 or newer)
- Python 3.6+
- Required Python packages:

```bash
pip install numpy opencv-python
```

---

## 🧠 How It Works

- Webots feeds camera frames into your Python controller.
- OpenCV processes the image and converts it to HSV color space.
- HSV thresholds are used to isolate yellow and red regions.
- Based on the detection, JetBot can move or print detection messages.

---

## 🎮 Movement Functions

| Function      | Description          |
|---------------|----------------------|
| `forward()`    | Move JetBot forward  |
| `backward()`   | Move backward        |
| `turn_left()`  | Rotate left          |
| `turn_right()` | Rotate right         |
| `stop()`       | Stop both wheels     |

---

## 🧪 Tips for Tuning

- Refine HSV values based on lighting:
  - Yellow: `[25, 150, 150]` to `[32, 255, 255]`
  - Red: `[0, 100, 100]`–`[10, 255, 255]` and `[160, 100, 100]`–`[179, 255, 255]`
- Use `cv2.imwrite()` to visualize what the JetBot sees and detects

---

## 📷 Optional Enhancements

- Draw bounding boxes on detected areas
- Follow colored objects based on position
- Add keyboard or manual override

---

## 🤝 Contributions

You're welcome to fork the repo, improve color handling, or integrate AI-based navigation!

---

## 📜 License

This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
