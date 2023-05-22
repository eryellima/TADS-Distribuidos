const WebSocket = require('ws');

const server = new WebSocket.Server({ port: 8080 });

let currentPlayer = 'X';
let gameBoard = [
  ['', '', ''],
  ['', '', ''],
  ['', '', ''],
];

function switchPlayer() {
  currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
}

function checkWinner() {
  const winningCombos = [
    // Linhas
    [gameBoard[0][0], gameBoard[0][1], gameBoard[0][2]],
    [gameBoard[1][0], gameBoard[1][1], gameBoard[1][2]],
    [gameBoard[2][0], gameBoard[2][1], gameBoard[2][2]],
    // Colunas
    [gameBoard[0][0], gameBoard[1][0], gameBoard[2][0]],
    [gameBoard[0][1], gameBoard[1][1], gameBoard[2][1]],
    [gameBoard[0][2], gameBoard[1][2], gameBoard[2][2]],
    // Diagonais
    [gameBoard[0][0], gameBoard[1][1], gameBoard[2][2]],
    [gameBoard[0][2], gameBoard[1][1], gameBoard[2][0]],
  ];

  for (const combo of winningCombos) {
    if (combo.every((symbol) => symbol === 'X')) {
      return 'X'; // Jogador X ganhou
    } else if (combo.every((symbol) => symbol === 'O')) {
      return 'O'; // Jogador O ganhou
    }
  }

  // Verificar se todas as células foram preenchidas (empate)
  const isBoardFull = gameBoard.every((row) => row.every((cell) => cell !== ''));
  if (isBoardFull) {
    return 'draw'; // Empate
  }

  return null; // Nenhum vencedor
}

function broadcastGameState() {
  const winner = checkWinner();

  const gameState = {
    currentPlayer,
    gameBoard,
    winner,
  };

  server.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(gameState));
    }
  });
}

server.on('connection', (socket) => {
  // Inicializar o jogo para o novo cliente
  socket.send(JSON.stringify({ currentPlayer, gameBoard }));

  socket.on('message', (data) => {
    const { row, col } = JSON.parse(data);

    // Atualizar o tabuleiro com a jogada do jogador atual
    gameBoard[row][col] = currentPlayer;

    // Alternar para o próximo jogador
    switchPlayer();

    // Verificar se há um vencedor ou empate
    const winner = checkWinner();

    // Enviar o estado atual do jogo para todos os clientes
    broadcastGameState();

    // Verificar se há um vencedor ou empate e enviar a mensagem correspondente
    if (winner) {
      server.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(JSON.stringify({ winner }));
        }
      });
    }
  });
});
