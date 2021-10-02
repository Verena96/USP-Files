#EP03

import random

def LeiaMatriz(NomeArq):
    
    
     # Lê e retorna uma matriz contendo todas as apostas da megasena.
     # Cada linha contém:
     # mat[][0] - int - número do sorteio
     # mat[][1] - str - data do sorteio
     # mat[][2..7] - int - cada número sorteado (1 a 60)
     # Retorna None se houve algum erro na leitura.
    mat = [] # inicia a matriz

     # abrir o arquivo para leitura
    try:
        
        arq = open(NomeArq, "r",encoding='utf-8')
            
        a = arq.read()
        
    except:
        
        print("Erro na abertura do arquivo (open)")
         
        return None
     # ler cada uma das linhas do arquivo
    i = 0

    for linha in a.split('\n')[:-1]:
        
        
     # se der alguma exception retorna None
        try:
            
            
            #lin = linha[:len(linha) - 1] # tira o \n do final
            v=linha.split('\t')# separa os elementos da string
            mat.append([]) # adiciona uma nova linha a matriz
            for j in range(8):

                if j == 1:

                    mat[i].append(v[1])
          
                else:

                    mat[i].append(int(v[j]))
           

            i = i + 1
        
        except:  
            
     # algum erro no trecho acima
            print("Erro no split(), no int() ou no append()")
            return None

     # consistência dos valores da matriz
     # ...
     # ...

     # fechar arquivo e retornar a matriz
    arq.close()
    return mat

#Funcao para escolher as apostas

def EscolheAposta(nt):
    
    #Nome do arquivo - deixei fixo com o dado pelo professor
    NomeArq = 'megasena2021.txt'
    
    #Prints solicitados
    print('Leitura do arquivo de sorteios')
    print('Montagem da tabela de último sorteio de cada número \n')
    print('Entre com o nome do arquivo:',NomeArq, '\n')
    print('Escolha de apostas \n')
    print('Quantidade de números da aposta:', nt)
    
    #Range de numeros de acordo com o valor nt
    lr = [random.randrange(1, 60) for i in range(nt)]
    
    print('Aposta escolhida - ',nt, 'números:')
    print(lr)
    
    while True:
        mat = LeiaMatriz(NomeArq)
        
        #Checa se todos os valores de m[2:] estao em lr
        result = [all(item in lr for item in m[2:]) for m in mat]

        if not any(result):
            print('*** Aposta válida')
            return True

        else:
            print('*** Aposta inválida')
            ind = [i for i, val in enumerate(result) if val][0] #index com valor True - valores ja sorteados
            s = mat[ind][0]
            d = mat[ind][1]
            print('*** Números já sorteados no sorteio {0} de {1}'.format(s,d))
            return False
        

#Teste
while True:
    nt = int(input('Escolha a quantidade de numeros da aposta:'))
    
    #Invalida inputs fora do intervalo
    if not 6<=nt<=12:
        print('Escolha número no intervalo [6-12]')
    
    else:    
        EscolheAposta(nt)

