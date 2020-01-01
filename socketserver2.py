import socket


# 建立一個socket套接字，該套接字還沒有建立連線
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 繫結監聽埠
server.bind(('localhost', 6688))
# 開始監聽，並設定最大連線數
server.listen(5)
# 獲取未建立連線的服務端的IP和埠資訊
print(server.getsockname())
# 下面註釋掉的是獲取未建立連線的服務端套接字的遠端IP和埠資訊，執行下面語句會報錯，原因就是現在還沒有遠端客戶端程式連線
# print(server.getpeername())

print(u'waiting for connect...')
# 等待連線，一旦有客戶端連線後，返回一個建立了連線後的套接字和連線的客戶端的IP和埠元組
connect, (host, port) = server.accept()
# 現在建立連線就可以獲取這兩個資訊了，注意server和connect套接字的區別，一個是未建立連線的套接字，一個是已經和客戶端建立了連線的套接字
peer_name = connect.getpeername()
sock_name = connect.getsockname()
print(u'the client %s:%s has connected.' % (host, port))
print('The peer name is %s and sock name is %s' % (peer_name, sock_name))

# 接受客戶端的資料
data = connect.recv(1024)
# 傳送資料給客戶端告訴他接收到了
connect.sendall(b'your words has received.')
print(b'the client say:' + data)

# 結束socket
server.close()
print("server close")
