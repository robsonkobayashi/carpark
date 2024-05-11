# carpark
Sistema de controle de acesso de veículos cadastrados: Script inicial apenas identifica a placa do carro e busca em um banco de dados fictício. Caso identifique, informa os dados cadastrados no BD. Se não está cadastrado irá descrever as informações (além de poder enviar a imagem junto se o sistema de mensagem aceitar)

# MELHORIAS FUTURAS

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
