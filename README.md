# Port Scanner com Python (Sockets) 🛡️

Criei este projeto para entender, na prática, como ferramentas de varredura (como o Nmap) funcionam "por baixo dos panos".

A ideia foi sair da teoria e escrever um script que interage diretamente com o protocolo TCP/IP. Em vez de apenas usar uma ferramenta pronta, desenvolvi a lógica de conexão socket para verificar manualmente se uma porta está aberta ou fechada.

## 🧠 O que aprendi com esse lab
* **Manipulação de Sockets:** Como criar conexões de rede "cruas" usando a biblioteca nativa do Python.
* **Lógica de Redes:** Entendi na prática o comportamento do *TCP Handshake*. Se o servidor não responde, a porta está fechada ou filtrada.
* **Tratamento de Erros:** Aprendi a usar `try/except` e timeouts para evitar que o script trave quando um IP não existe.

## ⚙️ Como funciona o script
O código recebe um IP alvo e uma lista de portas (ex: 21, 80, 443).
1. Ele tenta fazer uma conexão TCP (`socket.AF_INET, socket.SOCK_STREAM`).
2. Se a conexão for bem-sucedida (código 0), ele avisa que a porta está **ABERTA**.
3. A conexão é fechada imediatamente para economizar recursos.

## 🚀 Como testar
1. Clone este repositório.
2. Certifique-se de ter o Python 3 instalado.
3. Edite a variável `alvo` no script (pode testar com `localhost` ou `scanme.nmap.org`).
4. Rode no terminal:
   ```bash
   python scanner.py

