# Loop: printar o quadrado de cada número antecessor ao número dado, para números não-negativos i < n = i ^ 2

if __name__ == '__main__':
    n = int(input())

    # range(n) gera uma sequencia de n° inteiros de 0 até n-1. O laço for vai executar o codigo n vezes, 
    # atribuindo à variável i os valores de cada número na sequência.
    
    for i in range(n):    
        print(i*i)        # i ^ 2. como problema quer
        
