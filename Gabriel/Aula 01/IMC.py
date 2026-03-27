start = True
while True:
  try:

    nome = str(input("\nDigite seu nome: "))
    idade = int(input("\nDigite sua idade: "))
    peso = float(input("\ndigite seu peso: "))
    altura = float(input("\nDigite sua altura: "))

    if idade <20:
          print ("\nIdade insuficiente")
          continue


    if peso <= 0 or altura <= 0:
          print ("valores iválidos")
          continue

    imc = peso / (altura*2)

    if idade <= 60:

      if imc <18.5:
          faixa = "1"
      elif imc <25:
          faixa = "2"
      elif imc <30:
          faixa = "3"
      else: 
          faixa = "4"

    else:

      if imc <22:
          faixa = "1"
      elif imc <27:
          faixa = "2"
      elif imc <30:
          faixa = "3"
      else:
          faixa = "4"

    match faixa:
        case "1":
          classificação = "Baixo Peso"
        case "2":
          classificação = "Peso ideal"
        case "3":
          classificação = "Sobrepeso"
        case "4":
          classificação = "Obesidade"


    print ("\n#### Resultado ####")
    print ("\n Nome", nome)
    print ("\nIdade", idade)
    print ("\nIMC", round(imc,2))
    print ("\nClassificação", classificação)

    break
  except:
     print("\nValor informado é inválido")

  
  





      

