import socket

s = socket.socket()
s.bind(("0.0.0.0", 43156))
s.listen(1)  # clients permitted connect
print("server run")

sc, addr = s.accept()

while True:

    recibido = sc.recv(1024)
    if recibido == "quit":
        break

    print("received:", (recibido.decode()))
    break
    # sc.send(recibido)


print("bye")

sc.close()
s.close()
