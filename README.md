# CS 361 Sprint 2

Image Path Lookup Microservice: This microservice receives a string containing the name of a plant and returns the path to an image of that plant.The microservice communicates via ZeroMQ sockets.

## Socket Setup
To set up the socket, use the following code:
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```

## Request Data
To request data from the microservice, use the following code as a template. The 'request' variable will be
the name of the plant the microservice will look up.
```
request = input("Enter valid plant name: ")
socket.send_string(request)
```

## Receive Data
To receive data from the microservice, use the following code after the code above for requesting the data.
```
data = socket.recv_string()
```

## UML Diagram
<img width="595" alt="image" src="https://github.com/ACSadighi/cs361_sprint2/assets/108032145/e58305da-0f6b-448c-a736-a7527088fa44">
