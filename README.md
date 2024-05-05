# Hand-Tracking-MediaPipe-OpenCV

 - This repository hosts Python scripts designed for hand tracking and the storage of hand landmarks utilizing the robust capabilities of OpenCV and MediaPipe libraries. 
 - These scripts offer a comprehensive solution for real-time hand gesture recognition and analysis. Leveraging the advanced functionalities of MediaPipe, the scripts accurately detect and track 21 distinct landmarks on the human hand, facilitating precise spatial understanding.
 - Additionally, the scripts incorporate features for measuring Frames Per Second (FPS) on-screen, enhancing performance monitoring and optimization capabilities. Whether for academic research, interactive applications, or innovative projects, these scripts provide a versatile toolkit for exploring and leveraging hand tracking technologies in various domains.

![image](https://github.com/RAMAN0330/Hand-Tracking-MediaPipe-OpenCV/assets/83901587/cd640629-8cd3-4e59-9ba2-c133bc2ad89d)

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

## Description

This script utilizes the MediaPipe library to perform hand tracking and identify 21 landmarks on the hand. These landmarks include:

- WRIST = 0
- THUMB_CMC = 1
- THUMB_MCP = 2
- THUMB_IP = 3
- THUMB_TIP = 4
- INDEX_FINGER_MCP = 5
- INDEX_FINGER_PIP = 6
- INDEX_FINGER_DIP = 7
- INDEX_FINGER_TIP = 8
- MIDDLE_FINGER_MCP = 9
- MIDDLE_FINGER_PIP = 10
- MIDDLE_FINGER_DIP = 11
- MIDDLE_FINGER_TIP = 12
- RING_FINGER_MCP = 13
- RING_FINGER_PIP = 14
- RING_FINGER_DIP = 15
- RING_FINGER_TIP = 16
- PINKY_MCP = 17
- PINKY_PIP = 18
- PINKY_DIP = 19
- PINKY_TIP = 20

The script also calculates and prints the Frames Per Second (FPS) on the screen using the time module.

## Acknowledgements

This project acknowledges the invaluable contributions of the following libraries:

- [OpenCV](https://opencv.org/): An open-source computer vision and machine learning software library.
- [MediaPipe](https://mediapipe.dev/): A comprehensive, cross-platform framework for building perception pipelines.


## Installation
1) Clone this repository:
   ```bash
       git clone https://github.com/your_username/hand-tracking.git
       cd hand-tracking
2) Run the Python script:
    ```bash
       python main.py
3) You can install the required libraries using pip:
   ```bash
      pip install -r requirements.txt


