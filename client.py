import socket
import threading
import base64




def send_messages():#function to send messages
    while True:
        message = input("Your Message: ")
        # Send the encrypted message to the server
        client.send(bytes(message, 'utf-8'))

        if message.lower() == "quit":#if the message is quit, close the connection
            print("bye byee!!")
            client.close()
            break

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9969))

name = input("Enter your NICKNAME: ")
client.send(bytes(name, 'utf-8'))
print(client.recv(1024).decode())

# Create a thread to send messages
send_thread = threading.Thread(target=send_messages)
send_thread.start()

# Receive and display messages from the server
while True:
    response = client.recv(1024).decode()
    print("Server:", response)

   