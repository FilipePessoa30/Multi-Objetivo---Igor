import random

def gerar_problema_mochila(nome_arquivo, num_itens, capacidade, range_pesos, range_lucros):
    # Gerar pesos e lucros aleatórios dentro dos intervalos fornecidos
    pesos = [random.randint(range_pesos[0], range_pesos[1]) for _ in range(num_itens)]
    lucros = [random.randint(range_lucros[0], range_lucros[1]) for _ in range(num_itens)]
    
    # Salvar os dados no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"{num_itens}\n")
        arquivo.write(f"{capacidade}\n")
        arquivo.write(" ".join(map(str, pesos)) + "\n")  # Converter inteiros para strings
        arquivo.write(" ".join(map(str, lucros)) + "\n")  # Converter inteiros para strings

# Parâmetros para gerar o problema da mochila
nome_arquivo = "new_knapsack_data.txt"
num_itens = 100
capacidade = 10
range_pesos = (1, 8)  # Intervalo para os pesos dos itens
range_lucros = (1, 30)  # Intervalo para os lucros dos itens

# Gerar o problema da mochila e salvar no arquivo
gerar_problema_mochila(nome_arquivo, num_itens, capacidade, range_pesos, range_lucros)

print(f"Problema da mochila gerado e salvo em {nome_arquivo}")