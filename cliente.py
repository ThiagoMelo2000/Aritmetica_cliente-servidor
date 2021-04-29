from socket import *
import sys
import os
from time import sleep
# coding=UTF-8

host = gethostname()
port = 55551
cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))
    
while 1:
    
    arit = input('1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n0-Sair\n')
    
    if(arit == '0'):
        
        print("\nFinalizando o cliente...")
        sys.exit()
        
    elif(int(arit) < 4):
           
        cli.send(arit.encode())
        
        #SOMA
        num = input("Digite o primeiro número: ")
        cli.send(num.encode())
        num2 = input("Digite o segundo número: ")
        cli.send(num2.encode())

        retornoSoma = cli.recv(1024)
        
        print(retornoSoma.decode('utf8'))
        sleep(3)
        os.system('clear')

       
        
    else:
        
        print('Opção Inválida') 
        sleep(3)
        os.system('clear')