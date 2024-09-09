'''Importar a biblioteca multiprocessing para gerenciar múltiplos processos. A função soma_sublista é definida para calcular a soma de uma sublista. A função principal divide a lista original em sublistas menores com base no número de processos desejado. Se a divisão não for exata, os elementos restantes são adicionados à última sublista. Um pool de processos é criado para distribuir o trabalho de somar cada sublista de forma paralela, utilizando pool.map. Os resultados das sublistas são somados para obter o valor total. E no final mostra o tempo que o programa levou para processar.'''

import multiprocessing
import time

start_time = time.time() 

def soma_sublista(sublista): 
    return sum(sublista)

def soma_lista_paralelizada(lista, num_processos):
    tamanho_sublista = len(lista) // num_processos 
    sublistas = [lista[i*tamanho_sublista:(i+1)*tamanho_sublista] for i in range(num_processos)]

    if len(lista) % num_processos != 0:
        sublistas[-1].extend(lista[num_processos*tamanho_sublista:])
    
    with multiprocessing.Pool(processes=num_processos) as pool:
        resultados = pool.map(soma_sublista, sublistas)
    return sum(resultados)

if __name__ == "__main__":
    lista = [i for i in range(1, 50000000)]
    num_processos = 4
    end_time = time.time()
    processing_time = end_time - start_time
    soma = soma_lista_paralelizada(lista, num_processos)
    print(f"A soma total da lista é: {soma}")
    print(f"O tempo de processamento é igual a {processing_time:.1f} segundos")



