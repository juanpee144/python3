n1 = int (input ("Dime un número: "))
n2 = int (input ("Dime otro número: "))
division = n1 // n2
cociente = division
resto = n1 % n2
print (n1, "entre ", n2, "da un cociente ", round(division, 2), "y un resto ", resto)