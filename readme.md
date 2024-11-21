# Security Camera with Motion Detection

This project implements a basic security camera system using OpenCV and Haar Cascades for face and body detection. The system records video when motion (faces or bodies) is detected and saves the footage with a timestamped filename. The camera stops recording a few seconds after the detection ceases.

## Features:
- **Face and Body Detection**: Uses pre-trained Haar Cascade classifiers to detect faces and bodies in real time.
- **Motion-Triggered Recording**: The camera starts recording when motion is detected and stops a few seconds after no motion is detected.
- **Timestamped Video Saving**: The recorded video is saved with a filename that includes the current date and time.

## How It Works:
1. **Camera Capture**: The program continuously captures frames from the webcam.
2. **Detection**: It uses OpenCV’s Haar Cascade classifiers to detect faces and bodies.
3. **Recording**: Once motion is detected, the camera starts recording. It continues to record for a few seconds after motion stops.
4. **Save Video**: The recorded video is saved in the current directory with a timestamped filename.

## Code Overview

### Main Program (`main.py`)
The program uses OpenCV to access the webcam, detect faces and bodies, and manage video recording.

1. **Imports**:  
   - `cv2` for video capture and processing.
   - `time` and `datetime` for managing recording time and file naming.

2. **Video Capture Setup**:  
   - The webcam is accessed using `cv2.VideoCapture(0)`.
   - Haar Cascade classifiers are used to detect faces (`haarcascade_frontalface_default.xml`) and bodies (`haarcascade_fullbody.xml`).

3. **Motion Detection**:  
   - If a face or body is detected, recording is triggered.
   - If no motion is detected, the system waits for a set amount of time before stopping the recording.

4. **Recording**:  
   - The video is saved in the `.mp4` format with a timestamped filename.
   - The system continues to record as long as motion is detected, stopping a few seconds after motion ceases.

### Key Variables:
- **`scaleFactor`**: A parameter for detecting faces and bodies at multiple scales.
- **`frame_size`**: Determines the dimensions of the captured frame.
- **`seconds_record_after_detection`**: The time in seconds the camera will continue recording after motion is no longer detected.
- **`four_cc`**: Specifies the video codec for saving the video.
