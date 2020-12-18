from socket import *   

def server():
    port = int(input('채팅방 포트 :'))
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('',port))
    s.listen(1)
    print('연결 기다리는중...')
    connectionSock, addr = s.accept()
    print(str(addr), '에서 접속이 확인되었습니다.')
    print('recv(1024)')
    while True:
        data = connectionSock.recv(1024)
        print(addr," : ", data.decode())
        msg = input(">>")
        connectionSock.send(msg.encode())
        
def client():
    print('\n\n접속할 서버의 ip를 입력해주세요')
    ip = input('>>')
    print('접속할 서버의 port를 입력해주세요')
    port = int(input('>>'))
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(( ip ,port))
    print('연결 확인 됐습니다.\n\n')
    print('recv(1024)')
    while True:
        msg = input(">>")
        s.send(msg.encode())
        data = s.recv(1024)
        print(ip," : ",data.decode())


print('ip chat  v0.1    [made by Jay]')
print('-------------------------------')
print(' ip chat에 오신것을 환영합니다')
print('-------------------------------')
print(' 내 ip : ',gethostbyname(gethostname()))
while True:
    print('1. 채팅방 접속하기')
    print('2. 채팅방 만들기')
    print('3. 프로그램 종료')
    select = input('>>')
    if (select == '1'):
        client()
    elif (select == '2'):
        server()
    elif (select == '3'):
        quit()
    else:
        print('잘못 입력하셨습니다.\n\n')
