import os
import math

def main():
    os.system("clear")

    print("CALCULO DE LA HIPOTENUSA")
    print("========================")

    a = float(input("Cateto A:"))
    b = float(input("Cateto B:"))

    c = math.sqrt(a ** 2 + b ** 2)

    print(f"El triángulo cuyo Cateto A es {a:.2f} y cuyo Cateto B es {b:.2f} tiene una hipotenusa de {c:.2f}")

if __name__=='__main__':
    main()
