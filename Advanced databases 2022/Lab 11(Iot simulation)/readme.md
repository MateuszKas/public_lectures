


## Introduction

The aim of this laboratory is to familiarize participants with database management systems ([DBMS](https://en.wikipedia.org/wiki/Database#Database_management_system)) and the basic principles of their use in Industry 4.0. In these classes, we will use [SQLite](https://www.sqlite.org/index.html)




## Measurement collection system simulator

The main task of database systems is to collect data for easy processing and analysis. In this part of the workshop, we will present a measurement simulator that we will use in further exercises.

The simulator used in these workshops is very simple and consists of scripts:
```
- GenericSensor.py
- Client.py
- run_sim.py
```

GenericSensor.py is a class declaration that defines the structure of a sensor through fields:
1. name - sensor name, 
2. serial_number - sensor unique serial number, 
3. unit - measurements unit, 
4. min_val - minimal value from the sensor, 
5. max_val - maximum value from the sensor, 
6. fs - measurement frequency, 
7. lon - longitude, 
8. lat - latitude, 
9. ip_address - ip addres to communication with default value 'localhost', 
10. port - socket port number to comunication with default value None,

and enables it to be run as a separate thread that sends measurement information over the TCP/IP network on the appropriate port number.

run_sim.py script is used to run a multi-threaded program that simulates various sensors and their measurements. 



To run it, enter in the command line:

```
python run_sim.py
```
After successful activation, information about the created sensors will be displayed on the command line, for example:
```
name: temperature_1,
        serial_number: 2NixMVxg,
        ip_address: localhost,
        port:58080,
        unit:C,
        lon:19,
        lat:22
name: temperature_2,
        serial_number: 2VWFjDQW,
        ip_address: localhost,
        port:58081,
        unit:C,
        lon:19,
        lat:21
...
```

A file named iot_sensor_grid.csv will also be generated, containing a description of the generated sensor structure. Based on this file, the sensor network structure will be restored during the next program run.


Client.py script is used to read data from sensors. Before starting it, enter the appropriate ports in the __SensorConnection__ from the message above. For example:

```python
if __name__ == '__main__':
    sensor = SensorConnection(port=64363)
    
    sensor.start()
    
    while True:
        if len(sensor.buffer)>0:
            print(sensor.buffer.pop(0))
```
and enter in the console:
```
python Client.py
```
to start client.

If 

## Exercise:
1. Prepare a mechanism for reading data from all sensors in the file Client.py.
2. Suggest a database schema for the data from the measurement simulator
2. Implement your structure and collect data from sensors 


