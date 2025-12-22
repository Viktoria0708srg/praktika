#!/usr/bin/env python3
import socket

def check_service(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        
        if port in [80, 443]:
            s.send("HEAD / HTTP/1.0")
        banner = s.recv(1024).decode('utf-8', errors='ignore')
        s.close()
        
        if "HTTP" in banner or "Server:" in banner:
            return "Веб-сервер"
        elif "SSH" in banner:
            return "SSH сервер"
        elif port == 445:
            return "Windows SMB"
        elif port == 3389:
            return "RDP"
        elif banner:
            return "Открыт"
        else:
            return "Открыт (без баннера)"
    except:
        return "Закрыт"


ip = input("IP: ")
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389, 5900]

print(f"Сканирование {ip}...")
for port in ports:
    service = check_service(ip, port)
    print(f"Порт {port:4d}: {service}")

print("Готово!")