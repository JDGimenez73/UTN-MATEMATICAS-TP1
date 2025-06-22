def binario_4bits(n):
    return format(n, '04b')

def operacion_logica(a, b, op):
    if op == 'AND':
        return a & b
    elif op == 'OR':
        return a | b
    elif op == 'XOR':
        return a ^ b
    elif op == 'NAND':
        return ~(a & b) & 0b1111  # limitar a 4 bits
    elif op == 'NOR':
        return ~(a | b) & 0b1111
    elif op == 'XNOR':
        return ~(a ^ b) & 0b1111
    else:
        return None

def mostrar_operacion(a, b, op):
    resultado = operacion_logica(a, b, op)
    if resultado is None:
        print("Operación no válida.")
        return
    print(f"\nResultado de {op} bit a bit entre {a} y {b}:")
    print(f"Decimal: {resultado}")
    print(f"Binario: {binario_4bits(resultado)}")

def main():
    print("=== Calculadora Lógica Booleana de 4 bits ===")
    while True:
        try:
            a = int(input("Ingresá número A (0-15): "))
            b = int(input("Ingresá número B (0-15): "))
            if not(0 <= a <= 15) or not(0 <= b <= 15):
                print("Por favor, ingresá números entre 0 y 15.")
                continue
            print("Operaciones disponibles: AND, OR, XOR, NAND, NOR, XNOR")
            op = input("Elegí operación: ").upper()

            if op not in ['AND', 'OR', 'XOR', 'NAND', 'NOR', 'XNOR']:
                print("Operación inválida, intentá de nuevo.")
                continue

            mostrar_operacion(a, b, op)

            seguir = input("¿Querés hacer otra operación? (s/n): ").lower()
            if seguir != 's':
                print("¡Gracias por usar la calculadora!")
                break
        except ValueError:
            print("Entrada inválida, por favor ingresá números válidos.")

if __name__ == "__main__":
    main()
