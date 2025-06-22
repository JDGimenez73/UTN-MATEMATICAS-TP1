# 🧮 Calculadora Lógica Booleana de 4 Bits

## 📌 Descripción
Este proyecto consiste en una **calculadora lógica bit a bit** desarrollada en Python. Permite al usuario realizar operaciones lógicas entre dos números enteros del 0 al 15 (representados en binario de 4 bits), aplicando los conceptos de **álgebra de Boole**.

## 🎯 Objetivos

- Aplicar operaciones lógicas: `AND`, `OR`, `XOR`, `NAND`, `NOR`, `XNOR`.
- Mostrar resultados en **decimal y binario**.
- Validar entradas y operar de forma interactiva.
- Utilizar operadores bit a bit (`&`, `|`, `^`, `~`) y máscaras binarias.

---

## 🧠 Fundamento Matemático

Se utilizan los principios del **álgebra de Boole** para simular operaciones lógicas digitales:

| Operación | Símbolo Python | Descripción                           |
|-----------|----------------|---------------------------------------|
| AND       | `&`            | Devuelve 1 si ambos bits son 1        |
| OR        | `|`            | Devuelve 1 si al menos un bit es 1    |
| XOR       | `^`            | Devuelve 1 si los bits son distintos  |
| NAND      | `~(a & b)`     | Negación de AND                       |
| NOR       | `~(a | b)`     | Negación de OR                        |
| XNOR      | `~(a ^ b)`     | Negación de XOR                       |

> Se usa `& 0b1111` para limitar el resultado a 4 bits.

---

## ⚙️ Instrucciones de Uso

1. Ejecutar el programa con Python 3:
   ```bash
   python calculadora_logica.py
