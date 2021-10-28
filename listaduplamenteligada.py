# Nome: Verena C Saeta
# NUSP: 11306929
# Exercícios 3


class _Node:
    def __init__(self, info=None, prev=None, prox=None):
        self._info = info
        self._prev = prev
        self._prox = prox


class ListaDuplamenteLigada:
    def __init__(self):
        self._inicio = _Node(None, _Node(), _Node())
        self._final = _Node(None, _Node(), _Node())
        self._inicio._prox = self._final
        self._final._prev = self._inicio
        self._curr_iter_node = None
        self._tamanho = 0


    def Adiciona(self, info):
        for _node in self:
            if (True if _node._info is None else _node._info <= info) &\
               (True if _node._prox._info is None else _node._prox._info >= info):            
                _novo = _Node(info, _node, _node._prox)
                _node._prox._prev, _node._prox = _novo, _novo
                self._tamanho += 1
                break


    def Remove(self, info):
        _count = 0
        for _node in self:
            if _node._info == info:
                _node._prev._prox, _node._prox._prev = _node._prox, _node._prev
                self._tamanho -= 1
                _count += 1

        print('Foram removidos %d elementos.'%_count)


    def Conta(self, info):
        _count = 0
        for _node in self:
            if _node._info == info:
                _count += 1

        print('Foram Contados %d elementos.'%_count)


    def __str__(self):
        body = 'Nó   Anterior     Informação   Posterior\n'
        for _node_count, _node in enumerate(self):
            body += ('%d'%(_node_count + 1)).ljust(5) +\
                    (str(_node._prev._info)).ljust(13) +\
                    (str(_node._info)).ljust(13) +\
                    (str(_node._prox._info)).ljust(13) +\
                    '\n'
        return body


    def __iter__(self):
        self._curr_iter_node = _Node(None, None, self._inicio)
        return self


    def __next__(self):
        self._curr_iter_node = self._curr_iter_node._prox
        if self._curr_iter_node._prox is None:
            raise StopIteration
        return self._curr_iter_node
        

if __name__ == '__main__':
    ld = ListaDuplamenteLigada()
    print(ld)

    for i in range(5):
        ld.Adiciona('Maria')

    for i in range(3):
        ld.Adiciona('Joao')

    for i in range(2):
        ld.Adiciona('Antonio')

    print(ld)

    ld.Remove('Maria')

    print(ld)
    
    ld.Remove('Joao')

    print(ld)

    ld.Conta('Maria')
    ld.Conta('Antonio')
    ld.Conta('Joao')

