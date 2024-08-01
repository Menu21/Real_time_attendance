
# Real-Time Attendance System with Antispoofing

This project is a real-time attendance tracking system using surveillance cameras. It integrates YOLOv8 for image detection, DLIB for face recognition, and Firebase for managing the database. The system includes advanced antispoofing techniques to ensure accurate and secure attendance marking by distinguishing between genuine and fake images.

# Key Features
- Real-Time Attendance Tracking: Captures video feeds from surveillance cameras and marks attendance based on face recognition.
- Antispoofing Measures: Utilizes YOLOv8 for antispoofing to differentiate between real and fake faces, enhancing the security of the system.
- Face Recognition: Employs DLIB for reliable and efficient face recognition.
- Database Integration: Uses Firebase for storing and retrieving attendance data and student information.
- Training on Real Data: The antispoofing model is trained on a dataset consisting of real and fake images to ensure accuracy and reliability.

# Why YOLOv8?
- YOLOv8 (You Only Look Once version 8) is chosen for this project due to its superior performance in object detection tasks. It offers:

- High Accuracy: YOLOv8 provides accurate detection of faces and other objects in real-time, which is crucial for tracking and attendance marking.
- Speed: It is optimized for high-speed performance, allowing the system to process video feeds in real-time.
- Robustness: YOLOv8 is resilient to variations in image conditions, making it effective in diverse surveillance environments.

# Why DLIB for Face Recognition?
DLIB is selected for face recognition because of:

- Precision: DLIB’s face recognition model is known for its high accuracy and reliability in identifying individuals.
- Efficiency: It performs face recognition tasks efficiently, which is essential for real-time processing.
- Feature Extraction: DLIB provides robust feature extraction, improving the overall performance of face recognition.

# Why Firebase?
Firebase is used for its:

- Scalability: Firebase can handle the growing amount of data and user requests, making it suitable for dynamic and expanding projects.
- Real-Time Database: Provides real-time updates and synchronization across multiple devices, ensuring up-to-date attendance records.
- Ease of Integration: Simplifies the integration of authentication, storage, and database functionalities.
## Acknowledgements

 
This project uses the following libraries and tools:

- face_recognition: A powerful library for face recognition, provided by [ageitgey](https://github.com/ageitgey/face_recognition). This library is used for detecting and recognizing faces in images and video streams.

- YOLOv8: An advanced object detection model, provided by [Ultralytics](https://github.com/ultralytics/ultralytics). YOLOv8 is used for detecting objects in real-time, including face detection for anti-spoofing measures in this project.

- Firebase: A platform developed by [Google](https://firebase.google.com/) for creating mobile and web applications. Firebase is used for data storage and management in this project, allowing us to efficiently store and retrieve attendance data.



## Run Locally

Clone the project

```bash
https://github.com/Menu21/Real_time_attendance.git
```

STEP 01- Create a conda environment after opening the repository

```bash
conda create -n real python==3.10 -y
```

STEP 02- install the requirements

```bash
 pip install -r requirements.txt
```

Finally run the following command

```bash
python main.py
```

