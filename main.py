# main.py

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def main():
    print("=== Calculadora de Suma ===")
    print("Este es mi primer archivo Python subido a GitHub desde CMD y Git Bash.")
    
    try:
        x = float(input("Ingresa el primer número: "))
        y = float(input("Ingresa el segundo número: "))
        resultado = suma(x, y)
        print(f"La suma de {x} + {y} es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingresa solo números válidos.")

if __name__ == "__main__":
    main()
