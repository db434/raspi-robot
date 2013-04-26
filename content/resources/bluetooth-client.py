import bluetooth

#insert here the address of the Pi that you noted earlier
bd_addr = "00:15:83:0C:BF:EB"
#port must be consistent with server
port = 1

#create a socket and connect to the server
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

#we're now ready to send data!

#This will repeatedly send what a user types, you will probably want to 
#decide a format and check for it here so it can be easily decoded the 
#other side

while True:
	input = raw_input("what speeds would you like to set, e.g. 30,30 : ")
	if (input == "quit"):
		break
	else:
		sock.send(input)
#close up when finished
sock.close()
