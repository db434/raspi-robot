
import bluetooth
import i2c

#create a socket on bluetooth
#RFCOMM is one of several protocols bluetooth can use
server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

#choose a port number, must be same on client and server, 1 is fine
port = 1
#bind our socket to this port, the "" indicates we are happy to connect 
#on any available bluetooth adapter
server_sock.bind(("",port))
#listen for any incoming connections
server_sock.listen(1)

#accept connections and create the client socket
client_sock,address = server_sock.accept()
print("Accepted connection from ", address)

#Now is a good time to initialise our servos 
#maybe light an LED to indicate success as well
servos = i2c.I2C()

while True:
	#now everything is set-up we're ready to receive data
	data=client_sock.recv(1024)
	#print what we've received for debugging
	print( "received [%s]" % data)
	speeds= data.split(',')
	if (len(speeds) != 2):
		print("Data not valid speeds")
	else:
		try:
			i2c.setSpeeds(int(speeds[0]),int(speeds[1]))
		except ValueError:
			print("Data not valid speeds")
	#now we've got data it's up to you want you want to do with it!
	#We recommend sending tuples and decoding them as speeds to send
	#ensure client and server are consistent

#when finished be sure to close your sockets
client_sock.close()
server_sock.close()
