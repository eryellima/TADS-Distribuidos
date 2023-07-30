// Importa o módulo 'soap'
const soap = require('soap');

// Define a URL do WSDL para o serviço SOAP
const wsdlUrl = 'http://127.0.0.1:8000/?wsdl';

// Função para obter informações de um Pokemon a partir do ID
function getPokemon(pokemonId) {
  // Cria um cliente SOAP com base na URL do WSDL
  soap.createClient(wsdlUrl, function(err, client) {
    if (err) {
      console.error('Erro ao criar o cliente SOAP:', err);
      return;
    }

    // Chama o método 'get_pokemon' no serviço SOAP, passando o parâmetro 'pokemon_id'.
    client.get_pokemon({ pokemon_id: pokemonId }, function(err, result) {
      if (err) {
        console.error('Erro ao buscar pokemon:', err);
        return;
      }

    // Exibe as informações do Pokémon no console.
      console.log('Pokemon:', result);
    });
  });
}


// Obtém o argumento da linha de comando que indica o endpoint desejado.
const endpoint = process.argv[2];

// Verifica o endpoint que está usando
if (endpoint === 'pokemon') {
  const pokemonId = process.argv[3]; 
  getPokemon(pokemonId);
} else {
  console.error('Endpoint inválido!');
}
