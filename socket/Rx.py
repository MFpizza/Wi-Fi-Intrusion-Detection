import socket
import signal
import sys

def signal_handler(sig, frame):
    print('退出程序')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

HOST = '192.168.29.108'
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("等待连接...")
    conn, addr = s.accept()
    with conn:
        print('已连接到：', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # print('接收到的数据：', data.decode())
            