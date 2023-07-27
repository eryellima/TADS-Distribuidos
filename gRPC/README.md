# gRPC e GraphQL

## Tarefa

A tarefa consiste em desenvolver um pequeno projeto utilizando gRPC e GraphQL.

> Para rodar o projeto, você precisará executar o servidor gRPC em Python e o cliente gRPC em JavaScript separadamente. Vamos seguir os passos para cada um deles:

### Servidor gRPC em Python

1. Certifique-se de que você tenha o Python e as dependências instaladas. Se ainda não fez isso, instale o gRPC e outras bibliotecas necessárias:

```bash
pip install grpcio grpcio-tools graphene
```

2. Compile o arquivo `lol_champions.proto` para gerar os arquivos Python do gRPC:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. lol_champions.proto
```

3. Agora, execute o servidor Python usando o arquivo `server.py`. Abra um terminal e vá para o diretório onde está o arquivo `server.py`:

```bash
python server.py
```

Você verá a mensagem "Servidor iniciado na porta 50051..." indicando que o servidor está em execução e pronto para receber solicitações.

### Cliente gRPC em JavaScript

1. Certifique-se de que você tenha o Node.js instalado e as dependências instaladas para o cliente gRPC em JavaScript:

```bash
cd client
npm install grpc
```

2. Execute o cliente JavaScript usando o arquivo `client.js`. Abra outro terminal e vá para o diretório onde está o arquivo `client.js`:

```bash
node client.js
```

> Lembre-se de que o servidor gRPC em Python e o cliente gRPC em JavaScript precisam estar em execução simultaneamente para que a comunicação ocorra.
