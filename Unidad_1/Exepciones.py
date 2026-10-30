try:
    num1=float(input("Ingresa el primer numero: "))
    num2=float(input("Ingresa el segundo numero: "))
    resultado=num1/num2
    print(resultado)
except ZeroDivisionError:
    print("Error.No se puede dividir entre 0")
except ValueError:
    print("Error.No se puede poner una letra")
