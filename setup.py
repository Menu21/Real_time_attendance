from setuptools import find_packages, setup

setup(
    name='REAL_TIME_ATTENDANCE',
    version='0.0.0',
    author='Menu21',
    author_email='menkabharti2109@gmail.com',
    packages=find_packages(),
    install_requires=[
        'cmake',
        'dlib',
        'face_recognition',
        'cvzone',
        'opencv-python==4.5.4.60',
        'firebase_admin',
        'ultralytics',
        'mediapipe',
        'numpy==1.21.3'
    ],
)
