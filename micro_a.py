import os
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    plant = socket.recv_string()
    d = os.getcwd() + '/Cs361_PlantStore'
    images = os.listdir(d)
    plant_image = plant + '.jpg'
    path = 'Image not found'
    if plant_image in images:
        path = d + '/' + plant_image
    socket.send_string(path)
