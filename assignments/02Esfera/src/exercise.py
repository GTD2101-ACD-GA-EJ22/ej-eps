import os
import math

def main():
    os.system("clear")

    print("VOLUMEN DE UNA ESFERA")
    print("=====================")
    
    radio=float(input("Radio de la esfera:"))

    volumen = 4 / 3 * math.pi * radio ** 2

    print(f"El volumen de una esfera de radio {radio:.2f} es {volumen:.2f}")

if __name__=='__main__':
    main()
