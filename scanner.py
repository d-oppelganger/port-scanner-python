import socket

def scan_ports(ip_alvo, portas):
    print(f"\n--- Iniciando Varredura em: {ip_alvo} ---")
    
    for porta in portas:
        # 1. Cria o socket (o "telefone")
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. Define um tempo limite (para não travar se o alvo não responder)
        cliente.settimeout(0.5)
        
        # 3. Tenta conectar. O connect_ex retorna 0 se deu certo (aberta)
        codigo_retorno = cliente.connect_ex((ip_alvo, porta))
        
        if codigo_retorno == 0:
            print(f"[+] Porta {porta} está ABERTA!")
        else:
            # Opcional: print(f"[-] Porta {porta} fechada.")
            pass
            
        # 4. Fecha a conexão para liberar memória
        cliente.close()

if __name__ == "__main__":
    # Alvo: localhost (sua própria máquina)
    alvo = '127.0.0.1'
    
    # Lista de portas para testar. Adicionei a 50000 (do seu server) e outras comuns
    lista_portas = [21, 22, 80, 443, 50000]
    
    scan_ports(alvo, lista_portas)