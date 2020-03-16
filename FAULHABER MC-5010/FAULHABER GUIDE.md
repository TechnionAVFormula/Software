# FAULHABER mc-5010 guide
This guide is made to help beginners to get started with Faulhaber MC-5010 motor driver. It is based on the Faulhaber documentation and focuses on the needs of the Technion Formula AV. It is not a full tutorial but more like a reading guide walking you through Faulhaber documentation step by step with some additional notes.  
This guide is also meant to help relocate materials when working on the project.  

**Note:** the parts marked as <*(can be skipped)*>  are things that I think are not very important in the beginning but will be important later.


## Needed Material
All materials can be downloaded from Faulhaber website -> [MC-5010s](https://www.faulhaber.com/en/products/series/mc-5010-s/).

The material used in this document is:
* Quick Start Manual
* Drive Function
* Technical Manual
* Technical Information
* Communication Manual
* Programing Manual


## Learning Guide 

### Conceptual Structure  

The MC-5010 device is 'Motion Controller'. The software is 'Motion Manager'.

**'Technical Information'**  
- *p. 153-156*: Overview, fast reading is enough. Note: Structure diagram, operating modes, CANopen.

**'Drive Function'**  
- *p. 13-17*: Concept and structure.  
- *p. 19-27*: Drive state machine.


### Hardware Interface 

**'Technical Manual'**  
- *p. 11-14*: Physical connections (standard format only). Note: status led.
- *p. 24-32*: More details about ports. Note: first diagram on page 32. pins we will use M1, M2, X1, X2, X3, X4, X5.  
- (can be skipped) *p. 36-40*: Circuit diagrams. IO and CAN bus installation circuits. 


### Motion Manager

- Installing the software and using the software can be found in the **Quick Guide Manual'**.


### Motion Controller Configuration

**'Drive Function'**
- *p.32-33*: Control loops.
- (can be skipped) *p.36*: Current limits.
- (can be skipped) *p.40*: Speed limits.
- *p. 45-50*: Position control. Note: limits, monitoring.
- *p. 51-54*: Profile generator.
- *p. 73-79*: Factor group. Note: formulas, examples.
- *p. 90-92*: Analog inputs. Note: update rate 1ms, input voltage +-10, internal representation 10000=10V.
- (can be skipped) *p. 97-99*: Data save and restore.
- *p. 101-105*: Select operating mode. 
- *p. 106-108*: Profile Position mode. Note: example on page 110.
- (can be skipped) *p. 109,111-120*:  Multi set-points.
- (can be skipped) *p. 167-177*: Diagnosis - logging and error handling.
- *p. 178*: Status led.
- *p. 179-197*: Objects tables (useful). **Just ensure you understand how to use it.**


### Communication (CANopen)

**'Communication Manual'**
- *p. 8-11*: Overview - just read fast.
- *p. 14-16*: Basics and ID. Note: Ids that can/cannot be changed.
- *p. 17-19*: PDO. Focus on standard configuration.
- *p. 21-23*: SDO.
- (can be skipped) *p. 24-26*: Emergency object and sync.
- *p. 27-32*: Network Management.
- (can be skipped) *p. 36-39*: Trace.
- (can be skipped) *p. 40-42*: Settings via an network.
- *p. 43-52*: Objects tables (useful). **Just ensure you understand how to use it.**


### Programing  

- Read **'Programing Manual'**.


#
Written by Menashe Schwob for Technion Formula Autonomous Vehicle Project 2020.