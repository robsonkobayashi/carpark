# carpark
Com apenas uma foto do carro, você terá:

Identificação instantânea da placa: Nosso sistema de reconhecimento de imagens de última geração identifica a placa do veículo com precisão e rapidez.
Verificação de cadastro: Acesse um banco de dados completo e atualizado para saber se o veículo está devidamente registrado e em situação regular.
Descrição detalhada: Para veículos não cadastrados, obtenha uma descrição completa do carro, incluindo modelo, cor, ano e outros detalhes relevantes.

Ideal para:

Empresas e condomínios com garagens particulares: Identifique rapidamente invasores
Empresas de estacionamento: Controle o acesso de veículos à sua propriedade com segurança e eficiência.
Experimente agora e tenha a segurança que você precisa!

# MELHORIAS FUTURAS

Script inicial apenas identifica a placa do carro e busca em um banco de dados fictício. Caso identifique, informa os dados cadastrados no BD. Se não está cadastrado irá descrever as informações (além de poder enviar a imagem junto se o sistema de mensagem aceitar)

- Busca em banco de dados
- Envio de alerta para contato cadastrado no sistema
- Busca por semelhança
- Câmera com sensor de presença que aciona o script

# Como executar o script

- Instalar o python (testado na versão 3.10.12)
- Instalar as bibliotecas se necessário (pip install xxxx)
- Obter uma APIKEY no Google para usar a API da Gemini
- Configurar a APIKEY na variável de ambiente ou modificar a linha 15 (genai.configure(api_key=""))
- Modificar os valores do MY_DATABASE conforme arquivos de imagem que possuir
  Executar: python3 carpark.py ARQUIVO.jpg
