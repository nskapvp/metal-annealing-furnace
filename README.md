# Metal Annealing Furnace Control System

Bachelor’s project on modernization of the control system of an electric metal annealing furnace.

## Project goal

The goal of the project is to design a modern automation system for controlling the metal annealing process, including temperature control, protective gas control, pressure monitoring, SCADA visualization and recipe management.

## Architecture

The system consists of:

- PLC control logic
- SCADA/HMI visualization
- OPC UA communication
- PostgreSQL recipe database
- Python OPC UA client
- temperature, pressure and gas sensors
- actuators for heating and gas/pressure control

# Management system architecture: 
![image](https://github.com/user-attachments/assets/14073141-cf6e-411f-9689-b624737f0493)


# Example of screen forms (control panel):
![image](https://github.com/user-attachments/assets/fd8e3d82-9e51-48d5-bceb-c2398da58a3f)

## Repository structure

- pechka_codesys_control/ — PLC/CODESYS project
- FUXA/ — SCADA project files
- opcua-client/ — Python OPC UA client and recipe handling logic
- Пояснительная записка.docx — thesis documentation

## Main features

- staged annealing process
- recipe-based control
- temperature setpoints
- gas and pressure setpoints
- SCADA visualization
- OPC UA data exchange
- database-backed recipe storage

## Status

This is an educational bachelor’s project and engineering prototype. It is not intended to be used directly in production without additional validation, safety review and adaptation to real equipment.


