def raiz_cuadrada(numero: float | int) -> float:
    try:
        if not isinstance(numero, (int, float)):
            raise TypeError("El argumento debe ser un número.")
        if numero < 0:
            raise ValueError("El número no puede ser negativo.")
        resultado = numero ** 0.5
        print("La raíz cuadrada es:", resultado)
        return resultado
    except TypeError:
        print("Error: Debes introducir un número.")
    except ValueError:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")

raiz_cuadrada(-5)
