# Autonomous Robocar using Raspberry Pi Project

## Overview

This project is a Raspberry Pi-based robocar that provides manual control, obstacle avoidance, and line following capabilities. The project includes three iterations (`manual_mode.py`, `ir_sensor_obj_avoid.py`, and `linefol_objavoid.py`), each implementing different functionalities for controlling the robot.

## Project Structure

- `manual_mode.py`: Python script for manual control of the robot using the keyboard.
- `ir_sensor_obj_avoid.py`: Python script implementing obstacle avoidance using infrared sensors.
- `linefol_objavoid.py`: Python script combining line following and obstacle avoidance.

## Dependencies

- Python 3
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) library (for Raspberry Pi GPIO control)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/bhavikajangid1/final-year-project.git
cd final-year-project
```
### 2. Install Dependencies

Before running the project, you need to install the required Python libraries. Open a terminal on your Raspberry Pi and run the following command:

```bash
pip install RPi.GPIO
```
### 3. Hardware Setup

Before running the project, connect the necessary hardware components to your Raspberry Pi. The specific hardware requirements are as follows:

#### Hardware Components
- Motors
- Infrared Sensors 
- Ultrasonic Sensors 
- Motor Drivers for Front and Back Motors
- Any other peripherals required for your specific setup
  
#### Motor Connections
  ##### Front Motors 
    Connected to Motor Driver 1
      - Front-Left Forward: GPIO 17
      - Front-Left Backward: GPIO 18 
      - Front-Right Forward: GPIO 4
      - Front-Right Backward: GPIO 14
      
   ##### Back Motors
    Connected to Motor Driver 2
        - Back-Left Forward: GPIO 12
        - Back-Right Forward: GPIO 27 
        - Back-Left Backward: GPIO 5 
        - Back-Right Backward: GPIO 6
  
#### Motor Driver Connections
  - Connect the necessary wires to GPIO pins on the Raspberry Pi and the corresponding input pins on the motor driver for the front motors.
    
#### Sensor Connections
  ##### Infrared Sensors
    - Connect the left infrared sensor to GPIO 19
    - the right infrared sensor to GPIO 26.
  ##### Ultrasonic Sensors
    - Connect the left ultrasonic sensor to GPIO 2 (trigger) and GPIO 3 (echo)
    - Connect the right ultrasonic sensor to GPIO 20 (trigger) and GPIO 21 (echo).

  Make sure to double-check all connections before powering on your Raspberry Pi to avoid any potential damage.
  
### Additional Notes

- Make sure to double-check all connections before running the scripts to avoid potential hardware damage.
- If encountering issues, refer to the [Troubleshooting](#troubleshooting) section or open an issue on GitHub for assistance.

