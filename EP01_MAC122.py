# Exercício Programa I – MAC 122 – PDA
# Verena Christian Saeta
# NUSP: 11306929


import re

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return abs(a * b) / mdc(a, b)

class Pilha:
    def __init__(self, P=[]):
        self.P = P.copy()
        self.operadores = ['**', '*', '/', '+', '-']
        self.parentesis = ['(', ')']

    def empilhar(self, x):
        self.P.append(x)

    def desempilhar(self, ):
        if self.vazia(): return ''
        return self.P.pop() # ? 

    def __str__(self, ):#printa valor da pilha
        return str(self.P)

    def topo(self, ): #retorna valor do topo da pilha
        return self.P[-1] if not self.vazia() else None

    def __len__(self, ): #le o numero de termos da pilha
        return len(self.P)
    
    def vazia(self, ):
        return self.P == []
    
    def TraduzPosFixa(self, x):
        inf_exp = self.split_str(x)
        _saida = []
        for p in inf_exp:

            if p not in (self.operadores + self.parentesis):
                _saida.append(p)

            elif p == '(':
                self.empilhar(p)

            elif p == ')':
                topToken = self.topo()

                while pilha.topo() != '(':

                    # print('pilha antes do while:', self)
                    _saida.append(self.topo())
                    # print('saida:', _saida)
                    topToken = self.desempilhar()


                self.desempilhar()

            elif self.vazia():
                self.empilhar(p)

            else:
                while (self.topo() != '(' and self.prior(self.topo()) >= self.prior(p)):

                    # print('entrou no while')
                    _saida.append(self.desempilhar())


                self.empilhar(p)
                # print('pilha final:', self)

        for p in pilha.P[::-1]:
            _saida.append(p)

        return _saida
    
    def CalcPosFixa(self, x):
        
        try:
            _values = []
            for i in x:
                if i in self.operadores:
                    eq1 = _values[-2].split('/')
                    eq2 = _values[-1].split('/')

                    if len(eq1) == 1 and len(eq2) == 1 and i != '/':
                        _values = _values[:-2] + [str(eval(eq1[0] + i + eq2[0]))]

                    else:
                        if len(eq1) == 1: eq1.append('1')
                        if len(eq2) == 1: eq2.append('1')

                        if i == '*':
                            p = str(eval(eq1[0] + '*' + eq2[0]))
                            q = str(eval(eq1[1] + '*' + eq2[1]))
                        if i == '/':
                            p = str(eval(eq1[0] + '*' + eq2[1]))
                            q = str(eval(eq1[1] + '*' + eq2[0]))
                        if i == '+':
                            q = str(eval('mmc(' + eq1[1] + ',' + eq2[1] + ')'))
                            p1 = str(eval(eq1[0] + '*' + q + '/' + eq1[1]))
                            p2 = str(eval(eq2[0] + '*' + q + '/' + eq2[1]))
                            p = str(eval(p1 + '+' + p2))
                        if i == '-':
                            q = str(eval('mmc(' + eq1[1] + ',' + eq2[1] + ')'))
                            p1 = str(eval(eq1[0] + '*' + q + '/' + eq1[1]))
                            p2 = str(eval(eq2[0] + '*' + q + '/' + eq2[1]))
                            p = str(eval(p1 + '-' + p2))
                        if i == '**':
                            p = str(eval(eq1[0] + '**' + '(' + eq2[0] + '/' + eq2[1] + ')'))
                            q = str(eval(eq1[1] + '**' + '(' + eq2[0] + '/' + eq2[1] + ')'))

                        _values = _values[:-2] + [p + ' / ' + q]
                else:
                    _values.append(i)

            _res = [i.strip() for i in _values[0].split('/')]
            p = str(int(float(_res[0]))) if int(float(_res[0])) == float(_res[0]) else str(_res[0])
            if len(_res) == 1: return p
            if _res[1] == 1.: return p
            q = str(int(float(_res[1]))) if int(float(_res[1])) == float(_res[1]) else str(_res[1])
            return p + ' / ' + q
        except:
            return None
    
    def split_str(self, exp):
        res = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", exp)
        n_res = []
        for i in res:
            if len(n_res) > 0 and n_res[-1] == '*' and i == '*':
                n_res[-1] = '**'
            else:
                n_res.append(i)
        return n_res
    
    def prior(self, x):
        if x == '+': 
            return 2
        elif x == '-': 
            return 2
        elif x == '*': 
            return 3
        elif x == '/': 
            return 3
        elif x == '**':
            return 4
        elif x == '(': 
            return 1 # caso particular
        elif x == ')': 
            return 1 # caso particular
        else: 
            return 0 # não é operador



e=input("Insira a expressão numérica desejada:")
pilha = Pilha()
res = pilha.TraduzPosFixa(e)
#print(res)

res2 = pilha.CalcPosFixa(res)
print(res2)


