# -*- coding: utf-8 -*-

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 

if __name__ == '__main__':

    print("Insira os valores de cada item intercalado por espaços: ")
    val = list(map(int, input().split()))
    # val = [60, 100, 120]
    print("Insira os peso de cada item intercalado por espaços: ")
    wt = list(map(int, input().split()))
    W = int(input("Insira a capacidade da mochila: "))
    n = len(val) 
    print("A valor máximo que se pode carregar na mochila é: {}".format(knapSack(W, wt, val, n))) 