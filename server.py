import socket
import threading
import base64

# Function to handle client connections
def handle_client(client, addr):
    name = client.recv(1024).decode() # Receive client name
    print("Connected with", addr, name) # Print client name
    client.send(bytes("Welcome to the jungle!!", 'utf-8'))# Send welcome message to client

    while True:
        enc_text = client.recv(1024).decode()
        #if you remove the comments on the next two lines, the encoding will work
        #enc_text = enc_text.encode('ascii')
        #enc_text = base64.b64encode(enc_text).decode('ascii')

        if(enc_text == "emoji"):#if the message is emoji, replace it with :)
           
            enc_text = enc_text.replace("emoji",":)")
            print(name, ":", enc_text)
            break
        elif(enc_text == "sad"):#if the message is sad, replace it with :(
            enc_text = enc_text.replace("sad","(:")
            print(name, ":", enc_text)
            break

        print(name, ":", enc_text)  # Print Base64-encoded message

        # Check if the message is "quit"
        if enc_text.lower() == "quit":#if the message is quit, close the connection
            print("Client", name, "quit the chat")
            client.send(bytes("bye byee!!", 'utf-8'))
            client.close()
            break

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9969))
server.listen(4)
print('Waiting for a connection')

while True:
    
    client, addr = server.accept()#accept the connection

    client_thread = threading.Thread(target=handle_client, args=(client, addr))#create a thread for each client
    client_thread.start()