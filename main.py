from calculator import Calculation #I imported the calculation class
import os

calc = Calculation() #name given to Calculator class
continued = ('s','n', 'S', 'N') #tupla criada que tenha a opção de recomeçar ou quebrar
while True:
        
    operation = int(input("\t\tEscolha a operação:\n\t1 - (Soma)  2 - (Subtração)  3 - (Multiplicação)\n\t4 - (Divisão)  5 - (Potenciação) 6 - (Radiação)  \n\n\t\t"))
    while operation > 6: #if the whole number is greater than 6
        print("Tente novamente D;\n\n")
        break
    else: #if the integers are less than or equal to 6, you will be given two options of numbers you want to calculate
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        
        if operation == 1:
            result = calc.addition(num1, num2)
            print("O resultado da soma é: ", result)
        
        elif operation == 2:
            result = calc.subtraction(num1, num2)
            print("O resultado de subtração é: ", result)  
        
        elif operation == 3:
            result = calc.multiplication(num1, num2)
            print("O resultado da multiplicação: ", result)  
        
        elif operation == 4:
            result = calc.division(num1, num2)
            print("O resultado da divisão é:  ", result)
        
        elif operation == 5:
            result = calc.potentiation(num1, num2)
            print("O resultado da potenciação: ", result)
        
        elif operation == 6:
            result = calc.radiation(num1)
            print("O resultado da radiação é: ", result)
        
        continued = str(input("Deseja continua? [s/n]\n "))
        if continued == 's' or continued == 'S':
            continue
        elif continued == 'n' or continued == 'N':
            print("Até mais (:")
            break
else:
    print("Opção invalida!")
    continued = str(input("\tDeseja continua? [s/n]\n "))
