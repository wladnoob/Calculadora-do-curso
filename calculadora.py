nome = input("Olá! Para iniciarmos, digite aqui seu nome: ")
continuar = "Sim"

while continuar == "Sim":
  valor1 = input("Digite o primeiro valor: ")
  valor2 = input("Digite o segundo valor: ")

  print("Segue os resultados de adição, subtração, multiplicação, divisão, divisão exata e módulo:")
  print("Adição:", int(valor1) + int(valor2))
  print("Subtração:", int(valor1) - int(valor2))
  print("Multiplicação:", int(valor1) * int(valor2))
  print("Divisão:", int(valor1) / int(valor2))
  print("Divisão exata", int(valor1) // int(valor2))
  print("Módulo:", int(valor1) % int(valor2))

  resposta = input(nome+ ", você deseja continuar? (Sim/Não): ")
  if resposta == "Sim":
    pass
  else:
    continuar = "Não"
    print(nome+ ", muito obrigado por usar este programa.")