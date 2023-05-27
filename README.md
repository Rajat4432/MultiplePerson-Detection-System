# MultiplePerson-Detection-System 
The goal of the Multi-Person Detection System project is to provide a reliable and effective system for spotting several people in ATM situations. The technology uses computer vision techniques to recognise and track people who are in the vicinity of the ATM.
Requirements:
1.OpenCV
2.pyttsx3
3.Haar Cascade XML File
Working:
When the programme is launched, the computer's webcam or other attached camera is accessed, and frames from the video stream are continually captured by the system. The Haar cascade classifier is then used to identify faces in each frame, specifically using the "haarcascade_frontalface_default.xml" file.The number of faces that are continuously spotted by the programme is recorded. Using the pyttsx3 library, the system creates a voice command informing the user that only one person is permitted if more than one face is identified in a frame.
Note:
The "haarcascade_frontalface_default.xml" file from the Haar cascade should be put in the same directory as your Python script or programme.
