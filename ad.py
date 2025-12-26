from ldap3 import Server, Connection, NTLM # type: ignore

def simple_ad_check():
    
    domain = "base.com"
    username = "Администратор"
    password = "zxc!qwe!0708"
    
    try:
        
        server = Server(domain)
        conn = Connection(
            server, 
            user=f"{domain}\\{username}", 
            password=password,
            authentication=NTLM
        )
        
        if conn.bind():
            print(f"Успешное подключение к {domain}")
            print(f"Пользователь: {username} подключен")
            
            user_info = conn.extend.standard.who_am_i()
            print(f"Информация о сессии: {user_info}")
            
            domain_dn = ','.join([f"DC={part}" for part in domain.split('.')])
            
            conn.search(domain_dn, '(objectClass=user)', attributes=['cn'])
            print(f"Найдено пользователей: {len(conn.entries)}")
            
            conn.unbind()
            return True
        else:
            print("Ошибка: неверный логин или пароль")
            return False
            
    except Exception as e:
        print(f"Ошибка подключения: {str(e)}")
        return False

if __name__ == "__main__":
    print("Проверка подключения к Active Directory")
    simple_ad_check()