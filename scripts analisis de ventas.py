import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer archivo CSV
df = pd.read_csv("datos ventas.csv")

# Convertir fecha a formato fecha
df["fecha"] = pd.to_datetime(df["fecha"])

# Calcular importe de cada venta
df["importe"] = df["cantidad"] * df["precio"]

# Indicadores principales

ventas_totales = df["importe"].sum()

producto_mas_vendido = (
    df.groupby("producto")["cantidad"]
      .sum()
      .idxmax()
)

cantidad_producto = (
    df.groupby("producto")["cantidad"]
      .sum()
      .max()
)

# Ventas por mes

df["mes"] = df["fecha"].dt.to_period("M")

ventas_por_mes = (
    df.groupby("mes")["importe"]
      .sum()
)

# Crear carpeta resultados

os.makedirs("../resultados", exist_ok=True)

# Guardar CVS de resultados

ventas_por_mes.to_csv(
    "../resultados/ventas_por_mes.csv"
)

# Guardar resumen TXXT

with open(
    "../resultados/resumen_ventas.txt",
    "w",
    encoding="utf-8"
) as archivo:

    archivo.write(
        f"Ventas totales: ${ventas_totales:.2f}\n"
    )

    archivo.write(
        f"Producto más vendido: "
        f"{producto_mas_vendido} "
        f"({cantidad_producto} unidades)\n"
    )

# Genera grafico

plt.figure(figsize=(8,5))

ventas_por_mes.plot(marker="o")

plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Importe ($)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "../resultados/grafico_ventas.png"
)

plt.show()

# Muestra los resultados

print("VENTAS TOTALES")
print(ventas_totales)

print()

print("PRODUCTO MÁS VENDIDO")
print(producto_mas_vendido)

print()

print("VENTAS POR MES")
print(ventas_por_mes)