import socket


# 建立一個socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 主動去連線本機IP和埠號為6688的程序，localhost等效於127.0.0.1，也就是去連線本機埠為6688的程序
client.connect(('localhost', 6688))

# 接受控制檯的輸入
data = input()
# 對資料進行編碼格式轉換，不然報錯
data = data.encode('utf-8')
# 傳送資料
client.sendall(data)
# 接收服務端的反饋資料
rec_data = client.recv(1024)
print(b'form server receive:' + rec_data)

client.close()