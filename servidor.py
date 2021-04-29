from socket import *
import sys
# coding=UTF-8

host = gethostname()
port = 55551


print(f'HOST: {host} , PORT {port}')
serv = socket(AF_INET, SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)

while 1:
    
    con, adr = serv.accept()
    
    while 1:
        
        
        arit = con.recv(1024)
        num = con.recv(1024)
        num2 = con.recv(1024)
                
        if(arit == b''):
            
            print("\nFinalizando o servidor...")
            sys.exit()
        
        elif(arit == b'1'):
            #SOMA
           
            a = int(num)
            b = int(num2)
            
            soma = a + b

            con.sendall(("O valor da soma é: " + str(soma)).encode('utf-8'))
            
        elif(arit == b'2'):

            #SUBTRAÇÃO
                        
            a = int(num)
            b = int(num2)
            
            subt = a - b

            con.sendall(str("O valor da subtração é: " + str(subt)).encode('utf-8'))
            
        elif(arit == b'3'):

            #MULTIPLICAÇÃO
           
            a = int(num)
            b = int(num2)
            
            mult = a * b

            con.sendall(str("O valor da multiplicação é: " + str(mult)).encode('utf-8'))
            
        elif(arit == b'4'):

            #DIVISÃO
           
            a = int(num)
            b = int(num2)
            
            div = a / b

            con.sendall(str("O valor da divisão é: " + str(div)).encode('utf-8'))
            
        else:
            
            con.sendall(str("Opção inválida").encode('utf-8'))

        