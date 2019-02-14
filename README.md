# EC500-HealthMonitorSystem
Charles Thao's Health Monitor System Module Assembly for EC500

Original work from Huzefa's private repo: https://github.com/HuzefaMandvi/EC500-HealthMonitorSystem
## Responsibility:
I implemented encryption and decryption modules using Python Cryptography Library with Fernet

## Prerequisites:
   - Python >= 3.0
   - Tkinter
   - Cryptography

## Architecture: 
![Image of Architecture](https://i.imgur.com/bMbcV0x.jpg)

## Setup:
To run the application, run the following command in your Terminal:
```
python3 main.py

Input of this setup is a series of random numbers which would update every 10ms and the output is the user interface
```
## Pros:
Each session has a unique PID, and data in the session would be encrypted and compiled into a PID_data file. This way, patients' data is securely store for maximum confidentiality

The alert system works to inform physicians in case the patients' vitals drop below the acceptable range

The application in general runs smoothly without errors, and the interface is user-friendly
## Cons:
The user could not enter customized input, however, this is a design decision since it is better if the patient's vitals are measured constantly without any delay

## Room for improvement:
1. The simulator would be more interesting if the AI module/alert system is more robust (right now the design is very elementary)
2. Enable more interactive user experience with options of inputting other health stats like calculating BMI (age, weight and height) and medical history input to tune the AI module