start = True
while True:
  try:

    nome = str(input("\nDigite seu nome:"))
    idade = int(input("\nDigite sua idade: "))
    peso = float(input("\ndigite seu peso: "))
    altura = float(input("\nDigite sua altura:"))

    if idade <= 0 or peso <= 0 or altura <= 0:
      print("\nvalores inválidos:")
    else:
      imc = peso / (altura*2)

    if idade >= 20 and idade <= 60:

     if idade >20: 
      print ("\nIdade insuficiente")
     else:


      if imc < 18.5:
        faixa = "1"
      elif imc < 25:
        faixa = "2"
      elif imc < 30:
        faixa = "3"
      else:
        faixa = "4"

      match faixa:
        case "1":
          classificação = "Abaixo do peso"
        case "2":
          classificação = "Peso ideal"
        case "3":
          classificação = "Sobrepeso"
        case "4":
          classificação = "Obesidade"
        case _:
          classificação = "Erro"
    elif idade <60:

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
          classificação = "Abaixo do peso"
        case "2":
          classificação = "Peso ideal"
        case "3":
          classificação = "sobrepeso"
        case "4":
          classificação = "Obesidade"

    else:
      classificação = "classificção disponível a partir dos 20 anos"

    print ("\n#### RESULTDO ####")
    print ("\nNome,", nome)
    print ("\nIdade", idade)
    print ("\nIMC", round(imc,2))
    print ("\nClassificação", classificação)

  except:
    print ("\nValor inválido")

        
        

          
          





    