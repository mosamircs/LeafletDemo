import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print(host)
s.listen(5)                 # Now wait for client connection.
while True :
    c, addr = s.accept()     # Establish connection with client.
    print (addr)
    msg = "Thank you for your connection"
    c.send(msg.encode('utf-8'))
    c.close()                # Close the connection
