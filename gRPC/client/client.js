const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');

const PROTO_PATH = '../lol_champions.proto';
const packageDefinition = protoLoader.loadSync(PROTO_PATH);
const grpcObject = grpc.loadPackageDefinition(packageDefinition);
const championService = grpcObject.lol.ChampionService;

const client = new championService('localhost:50051', grpc.credentials.createInsecure());

function getChampionInfo(name) {
  const request = { name: name };
  client.GetChampionInfo(request, (err, response) => {
    if (err) {
      console.error('Erro:', err);
      return;
    }
    console.log('Informações do Campeão:');
    console.log('Nome:', response.name);
    console.log('Função:', response.role);
    console.log('Dificuldade:', response.difficulty);
    console.log('Habilidades:', response.abilities.join(', '));
  });
}

// Troque para o nome de outro campeão, se desejar.
const championName = 'Aatrox'; 
getChampionInfo(championName);
