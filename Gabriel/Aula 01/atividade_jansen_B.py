while True:
  try:
    raio = float(input("\ndigite o raio: "))
    if raio <= 0:
       print ("\nO raio deve ser maior que zero: ")
       continue
    break
  except ValueError:
    print("\ndigite um número válido:")

Circumferencia = 2*3.14*raio
print ("\nO raio da circumferencia é", Circumferencia )


