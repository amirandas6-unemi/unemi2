# Calculadora de IMC (Índice de Masa Corporal) con gráfico de barras
import matplotlib.pyplot as plt

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad grado I"
    elif 35 <= imc < 39.9:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

# Programa principal
print("===== CALCULADORA DE IMC =====")

# Pedir datos al usuario
peso = float(input("Ingrese su peso en kilogramos (kg): "))
altura = float(input("Ingrese su estatura en metros (m): "))

# Calcular IMC
imc = calcular_imc(peso, altura)
categoria = clasificar_imc(imc)

# Mostrar resultados
print(f"\nSu IMC es: {imc:.2f}")
print(f"Clasificación: {categoria}")

# Visualización con diagrama de barras
categorias = [
    "Bajo peso",
    "Peso normal",
    "Sobrepeso",
    "Obesidad grado I",
    "Obesidad grado II",
    "Obesidad grado III"
]

valores = [1 if cat == categoria else 0 for cat in categorias]
colores = ["#1f77b4" if cat != categoria else "#ff7f0e" for cat in categorias]

plt.figure(figsize=(8, 5))
plt.bar(categorias, valores, color=colores)
plt.title("Clasificación IMC")
plt.xlabel("Categoría")
plt.ylabel("Resultado")
plt.ylim(0, 1.2)
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
