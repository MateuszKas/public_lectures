import socket
import threading            
 
class SensorConnection(threading.Thread):
    def __init__(self, port, ip_address='localhost') -> None:
        threading.Thread.__init__(self)
        self.port = port
        self.ip_address = ip_address
        self.sensor_socket = socket.socket()
        self.buffer = []
    
    def run(self):
        try:
            self.sensor_socket.connect((self.ip_address, self.port))
            while True:
                self.buffer.append(self.sensor_socket.recv(1024).decode())
        except:
            self.sensor_socket.close()

if __name__ == '__main__':
    sensor = SensorConnection(port=64363)
    
    sensor.start()
    
    while True:
        if len(sensor.buffer)>0:
            print(sensor.buffer.pop(0))