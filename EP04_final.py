#EP04
from random import seed, randrange

# Gera n números aleatórios no intervalo [a, b)
def GeraAmostra(a, b, n):
    
    # Use o seu NUSP como semente
    NUSP = 1234567
    seed(11306929)
    amostra = n * [0]
    
    for k in range(n):
        
         amostra[k] = a + float(randrange(1000000)) * (b - a)/1000000.0
            
    return amostra


class Done(Exception): pass



def Func(a,b,n):
    

    i = input('Entre com a quantidade de intervalos:')



    try:
        float(a)
    except:
        print('Erro --- Digite um valor numérico para a')
        raise Done


    try:
        float(b)
    except:
        print('Erro --- Digite um valor numérico para b')
        raise Done


    try:
        int(n)
    except:
        print('Erro --- Digite um valor inteiro para n')
        raise Done

    
    try:
        int(i)
    except:
        print('Erro --- Digite um valor inteiro para quantidade de intervalos')
        raise Done

    


    a = float(a)
    b = float(b)
    n = int(n)
    i = int(i)
    
    if (i <= 0  or n <= 0): 
        print('Erro --- Digite um valor maior que zero para a quantidade de intervalos/ elem da amostra')
        raise Done


    if (b<=a):

        print('Erro --- Digite um valor de b maior que a.')
        raise Done


    if (b-a)/n < 0.001:
        print('Erro --- Intervalo precisa ser maior que 0.001.')
        raise Done



    am = GeraAmostra(a, b, n)

    print('\n','Amostra:','\n')
    for k in range(n):

        if k % 5 == 4: print("%10.5f" %am[k])
        else: print("%10.5f" %am[k], end = ' ')


    l1 = []
    lim_inf = a
    lim_sup = b
    iv = i
    r = (lim_sup - lim_inf)/iv
    vr = lim_inf+r

    while vr <= lim_sup:

        #Count of elements in interval
        c = len([z for z in am if lim_inf<=z<vr])

        #Append data into list
        l1.append((lim_inf,vr,c))

        #Update interval boundries
        lim_inf = round((lim_inf+r),3)
        vr = round((vr+r),3)

    print('\n')
    print("Intervalo\t\t Frequência\t\t Gráfico")

    for i in range(len(l1)):

        print('{0:.3f} A {1:.3f} \t\t {2} \t\t\t {3}'.format(l1[i][0], l1[i][1], l1[i][2],l1[i][2]*"\u2586"))
    


def execute():
    a = input('Limite inferior:')
    b = input('Limite superior:')
    n = input('Entre com a quantidade de elementos da amostra:')
    try:
        while True:
            Func(a,b,n)

    except Done:
        execute()



execute()

