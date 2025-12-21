#!/usr/bin/env python3
import socket

def check_port(ip, port):
    sock = socket.socket()
    try:
        sock.connect((ip, port))
        sock.close()
        return True
    except:
        return False

ports_to_check = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389, 5900]

ip = input("Введите IP-адрес: ")

print(f"Сканирование {ip}...")

for port in ports_to_check:
    if check_port(ip, port):
        print(f"Порт {port}: ОТКРЫТ")
    else:
        print(f"Порт {port}: закрыт")
print("Готово!")


     
    

