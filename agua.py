def calcular_consumo_agua(peso, genero):
    if genero.lower() == 'homem':
        consumo_agua_litros = peso * 0.035
    elif genero.lower() == 'mulher':
        consumo_agua_litros = peso * 0.031
    else:
        raise ValueError("Gênero inválido. Use 'homem' ou 'mulher'.")
    
    return consumo_agua_litros

# Exemplo de uso:
peso_usuario = float(input("Digite o seu peso (em kg): "))
genero_usuario = input("Digite o seu gênero (homem/mulher): ")

try:
    consumo_recomendado = calcular_consumo_agua(peso_usuario, genero_usuario)
    print(f"A quantidade recomendada de água para você é de {consumo_recomendado:.2f} litros por dia.")
except ValueError as e:
    print(str(e))



