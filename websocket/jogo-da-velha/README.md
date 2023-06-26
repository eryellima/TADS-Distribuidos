# Desenvolvimento de Sistemas Distribuídos
## WebSocket
WebSocket é uma tecnologia que permite a comunicação por canais full-duplex sobre um único soquete Trasmission Control Protocol (TCP).

## Tarefa
- A tarefa era desenvolver um estudo de caso que fizesse uso do WebSocket.

O projeto foi desenvolvido usando `Node.js`, além da biblioteca `ws` para o Node.
Foi criado um jogo da velha, onde dois clientes jogam um sendo o jogador 'X' e o outro 'O'.
O projeto ainda possui algumas defeitos em relação a verificações, como verificação de empates que pretendo ajustar mais a frente

## Subindo o Server
Você consegue subir servidor para testalo através do comando:
~~~~
node server.js
~~~~
> neste momento você pode ver se o o servidor está funcionando entrando em <localhost:3000> assim como abrin o arquivo `index.html` direto no navegador.

###### OBS
Talvez seja preciso instalar as dependencias usadas no projeto que pode ser encontrada no arquivo `package.json`

Instalação da biblioteca ws:
```
    npm install ws
```
