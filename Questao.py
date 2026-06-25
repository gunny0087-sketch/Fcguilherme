
estatura1 = float(input("Digite  a primeira estatura: "))
estatura2 = float(input("Digite a segunda estatura: "))
estatura3 = float(input("Digite a terceira estatura: "))
if  estatura1 == estatura2 or estatura1 == estatura3 or estatura2 == estatura3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")
else:
  if estatura1 > estatura2 and estatura1 > estatura3:
        print("A maior estatura é:", estatura1)
  elif estatura2 > estatura1 and estatura2 > estatura3:
        print("A maior estatura é:", estatura2)
  else:
        print("A maior estatura é:", estatura3)
