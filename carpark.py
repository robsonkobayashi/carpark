import os # se for ler a APIKEY das variáveis de ambiente
import sys
import google.generativeai as genai
import PIL.Image

MY_DATABASE = [ ["POX4G21", "PRATA", "VOLKSWAGEN", "POLO"],
                ["AAA5555", "BRANCO", "VOLKSWAGEN", "FUSCA"],
                ["BRA0S17", "PRATA", "VOLKSWAGEN", "GOL"],
                ["AJB0E96", "BRANCO", "ANTIGO", "ANTIGO"],
                ["BRA2E19", "PRATA", "CHEVROLET", "OPALA"],
                ["CDV2172", "PRETO", "CHEVROLET", "ASTRA"]
                
            ]
#STEPSFILE = "steps.txt"
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
#genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# genai.configure(api_key=userdata('GOOGLE_API_KEY'))

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

filename_img = 'placa/POX4G21.jpeg'

#verifica se foi informado um arquivo para leitura
if len(sys.argv) > 1:
  filename_img = sys.argv[1]

#
img = PIL.Image.open(filename_img)#jpg???
response = model.generate_content(["Qual a placa do carro (apenas letras e números)?", img], stream=True)
response.resolve()
#print(response.text)
placa = response.text
placa = placa.strip().upper()

for car in MY_DATABASE:
  if car[0] == placa:
    print(f"OK: cor={car[1]}, marca={car[2]}, modelo={car[3]}")
    #print("OK")
    placa = ""
    break

if placa != "":
    response = model.generate_content(["Descreva o carro da imagem", img], stream=True)
    response.resolve()
    #print(response.text)
    print(response.text)