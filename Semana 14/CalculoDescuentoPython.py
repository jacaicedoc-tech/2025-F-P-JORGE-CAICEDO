# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento de una compra.
    :param monto_total: float, monto total de la compra
    :param porcentaje_descuento: float, porcentaje de descuento (10% por defecto)
    :return: float, monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
def main():
    # --- Primera llamada a la función ---
    # Solo se pasa el monto, usa el 10% por defecto
    monto1 = 150.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1

    print("Compra 1")
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"Total a pagar: ${total1:.2f}")
    print("-" * 30)

    # --- Segunda llamada a la función ---
    # Se pasa el monto y un porcentaje específico
    monto2 = 300.0
    porcentaje2 = 20
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total2 = monto2 - descuento2

    print("Compra 2")
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
    print(f"Total a pagar: ${total2:.2f}")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()

