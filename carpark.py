import os # se for ler a APIKEY das variáveis de ambiente
import sys # para obter os argumentos da linha de comando
import google.generativeai as genai # para acessar a gemini
import PIL.Image # para manipular imagens

MY_DATABASE = [ ["AAA4G21", "PRATA", "VOLKSWAGEN", "POLO"],
                ["AAA5555", "BRANCO", "VOLKSWAGEN", "FUSCA"],
                ["BBB0S17", "PRATA", "VOLKSWAGEN", "GOL"],
                ["AAA0E96", "BRANCO", "ANTIGO", "ANTIGO"],
                ["BBB2E19", "PRATA", "CHEVROLET", "OPALA"],
                ["CCC2172", "PRETO", "CHEVROLET", "ASTRA"]
                
            ]

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
# genai.configure(api_key=userdata.get('GOOGLE_API_KEY'))

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}    

safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
}

model = genai.GenerativeModel(model_name='gemini-pro-vision',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)

filename_img = 'placa/AAA4G21.jpeg' # Foto default para teste rápido

# Verifica se foi informado um arquivo para leitura
if len(sys.argv) > 1:
  filename_img = sys.argv[1]

img = PIL.Image.open(filename_img) # Abre a foto (testado com jpeg e png)
response = model.generate_content(["Qual a placa do carro (apenas letras e números)?", img], stream=True)
response.resolve() # Aguarda o processamento
placa = response.text # Obtém a informação textual
placa = placa.strip().upper() # Normaliza os dados de busca

# Busca no database
for car in MY_DATABASE:
  if car[0] == placa:
    print(f"OK: cor={car[1]}, marca={car[2]}, modelo={car[3]}")
    #print("OK")
    placa = ""
    break

# Se a placa não está cadastrada, avisa o responsável. 
# TODO: enviar msg pro responśavel
if placa != "":
    response = model.generate_content(["Descreva o carro da imagem", img], stream=True)
    response.resolve()
    #print(response.text)
    print(f"Veículo não identificado. Placa: {placa}. Detalhes extras: {response.text}")
