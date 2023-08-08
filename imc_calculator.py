def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def interpretar_categoria(imc):
    if imc < 16.0:
        return "Subpeso Severo"
    elif 16.0 <= imc < 16.9:
        return "Subpeso Moderado"
    elif 17.0 <= imc < 18.4:
        return "Subpeso Leve"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25.0 <= imc < 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc < 39.9:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"

def main():
    while True:
        try:
            peso = float(input("Digite o seu peso (em kg): "))
            altura_cm = float(input("Digite a sua altura (em centímetros): "))

            altura_m = altura_cm / 100  # Altura de cm para m
            imc = calcular_imc(peso, altura_m)
            categoria = interpretar_categoria(imc)

            print(f"Seu IMC é: {imc:.2f}")
            print(f"Categoria: {categoria}")
            break  # Quebra o loop se valor incorreto

        except ValueError:
            print("Por favor, digite um valor válido para peso e altura.")

if __name__ == "__main__":
    main()