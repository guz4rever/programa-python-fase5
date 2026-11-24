# --------------------------------------------------------
# Fase 5 - Evaluación Final POA
# Problema 3: Reabastecimiento de Inventario
# Autor: Santiago Guzmán López
# --------------------------------------------------------

# Matriz de inventario
# Formato:
# [Código, Nombre del artículo, Stock actual, Stock mínimo]

inventario = [
    ["A001", "Mouse", 10, 15],
    ["A002", "Teclado", 5, 5],
    ["A003", "Monitor", 2, 6],
    ["A004", "Cámara", 20, 15],
    ["A005", "Audífonos", 1, 8]
]

# Función para calcular la cantidad que debe solicitarse
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Encabezado del informe
print("=" * 55)
print("      INFORME DE REABASTECIMIENTO DE INVENTARIO")
print("=" * 55)

# Recorrido de la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print(f"\nCódigo: {codigo}")
    print(f"Artículo: {nombre}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock mínimo: {stock_minimo}")
    print(f"Cantidad a solicitar: {cantidad_pedir}")

print("\nFin del informe.")