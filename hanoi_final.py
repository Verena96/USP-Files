def Hanoi(n, torreA, torreB, torreAux, *hanoi_args, orig=True):
    if orig:
        pos = {'0': list(range(n, 0, -1)), '1': [], '2': []}
        hanoi_args = (n, pos)
    if n == 1:
        # mover disco 1 da torreA para a torreB
        Movimente(1, torreA, torreB, *hanoi_args)
    else:
        # n - 1 discos da torreA para torreAux com torreB auxiliar
        Hanoi(n - 1, torreA, torreAux, torreB, *hanoi_args, orig=False)
        # mover disco n da torreA para torreB
        Movimente(n, torreA, torreB, *hanoi_args)
        # n - 1 discos da torreAux para a torreB com torreA auxiliar
        Hanoi(n - 1, torreAux, torreB, torreA, *hanoi_args, orig=False)

    
def Movimente(k, origem, destino, *args):
    print("mover disco ", k, " da torre ", origem, " para a torre ", destino)
    peca = args[1][str(origem)].pop()
    args[1][str(destino)].append(peca)
    if len(args) > 0: # print torres
        base = [list('ABC')]
        for i in range(args[0]):
            values = [str(args[1][k][i]) if len(args[1][k]) > i else ' ' for k in ['0', '1', '2']]
            base.append(values)
        txt = ''
        for b in base[::-1]:
            txt += ' '.join(b) + '\n'
        print(txt)

print("\n* * * Movimentar 2 discos * * *")
Hanoi(2, 0, 1, 2)

print("\n* * * Movimentar 3 discos * * *")
Hanoi(3, 0, 1, 2)
