import requests
import json
print('###################')
print('#Jogo de Perguntas#')
print('###################')
pergunta1 = requests.get('https://covid19-brazil-api.vercel.app/api/report/v1/New%20Zealand')
perguntas1 = json.loads(pergunta1.text) 

print("Qual o pais possui o menor número de casos do COVID 19?")
print("1- Brasil")
print("2- Nova Zelândia ")

resposta1 = int(input('Digite sua resposta:'))
print()
pontos= 0

if(resposta1==1):
  print("Você errou!")
  print()
else:
  if(resposta1==2):
    print("Você Acertou!!!")
    print()
    print('Nome do País:', perguntas1["data"]["country"])
    print('Número de Casos:', perguntas1["data"]["cases"])
    pontos += 5
    print()


pergunta2 = requests.get('https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/rr')
perguntas2 = json.loads(pergunta2.text) 

print("Qual o estado possui o maior número de casos do COVID 19?")
print("1- Roraima")
print("2- São Paulo")

resposta2 = int(input('Digite sua resposta:'))
print()
if(resposta2==2):
  print("Você errou!")
  print()
else:
  if(resposta2==1):
    print(" Você Acertou!!!")
    print()
    print('Nome do Estado:', perguntas2["state"])
    print('Número de Casos:', perguntas2["cases"])
    pontos += 5
    print()

pergunta3 = requests.get('https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/ma')
perguntas3 = json.loads(pergunta3.text) 

print("Qual o estado possui o menor número de casos do COVID 19?")
print("1- Rio de Janeiro")
print("2- Maranhão")

resposta3 = int(input('Digite sua resposta:'))
print()
if(resposta3==1):
  print("Você errou!")
  print()
  
else:
  if(resposta3==2):
    print(" Você Acertou!!!")
    print()
    print('Nome do Estado:', perguntas3["state"])
    print('Número de Casos:', perguntas3["cases"])
    pontos += 5
    print()
    
pergunta4 = requests.get('https://covid19-brazil-api.vercel.app/api/report/v1/US')
perguntas4 = json.loads(pergunta4.text) 

print("Qual país possui o maior número de casos do COVID 19?")
print("1- India")
print("2- Estados Unidos")

resposta4 = int(input('Digite sua resposta:'))
print()
if(resposta4==1):
  print("Você errou!")
  print()
  
else:
  if(resposta4==2):
    print(" Você Acertou!!!")
    print()
    print('Nome do País:', perguntas4["data"]["country"])
    print('Número de Casos:', perguntas4["data"]["confirmed"])
    pontos += 5
    print()
      

pergunta5 = requests.get('https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/rr')
perguntas5 = json.loads(pergunta5.text) 

print("Qual estado possui o maior número de mortos do COVID 19?")
print("1- Roraima")
print("2- Amapá")

resposta5 = int(input('Digite sua resposta:'))
print()
if(resposta5==1):
  print("Você Acertou!")
  pontos += 5
  print()
  
else:
  if(resposta5==2):
    print(" Você Errou!!!")
    print()
    print('Nome do Estado:', perguntas5["state"])
    print('Número de Mortos:', perguntas5["deaths"])
    print()
      

pergunta6 = requests.get('https://covid19-brazil-api.vercel.app/api/report/v1/Solomon%20Islands')
perguntas6 = json.loads(pergunta6.text) 

print("Qual país possui o menor número de mortos do COVID 19?")
print("1- Finlandia")
print("2- Ilhas Salomão")

resposta6 = int(input('Digite sua resposta:'))
print()
if(resposta6==1):
  print("Você Errou!")
  print()
  print("Sua pontuação total é", pontos)
else:
  if(resposta6==2):
    print(" Você Acertou!!!")
    print()
    print('Nome do País:', perguntas6["data"]["country"])
    print('Número de Mortos:', perguntas6["data"]["deaths"])
    pontos += 5
    print()
    print("Sua pontuação total é", pontos)   


