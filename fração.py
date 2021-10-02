# Nome: Verena Christian Saêta
# NUSP: 11306929
# Exercícios 1

class Fração:
    
    '''Define a classe Fração Ordinária.'''
    
    def __init__(self, topo = 0, base = 1):
        
        if base == 0:
            raise ValueError("Denominador igual a zero")
        
        if type(topo) != int:
            topo = int(topo)
        
        if type(base) != int:
            base = int(base)
        
        self.num = topo #numerador
        self.den = base #denominador
        
    def simplify(self):
        
        common = mdc(self.num, self.den)
        novo_num = self.num // common
        novo_den = self.den // common
        
        return Fração(novo_num,novo_den)
        
    # função mdc
    def mdc(n, m):
    
        resto = n % m
        while resto != 0:
            n = m
            m = resto
            resto = n % m
        return m
        

    def __add__(self, f2):
        
        xnum = self.num * f2.den + self.den * f2.num
        xden = self.den * f2.den
        xmdc = Fração.mdc(xnum, xden)
        
        return Fração.simplify(Fração(xnum // xmdc, xden // xmdc))
    
    def __sub__(self, f2):
        
        xnum = self.num * f2.den - self.den * f2.num
        xden = self.den * f2.den
        xmdc = Fração.mdc(xnum, xden)
        
        return Fração.simplify(Fração(xnum // xmdc, xden // xmdc))
    
    def __mul__(self, f2):
        
        xnum = self.num * f2.num
        xden = self.den * f2.den
        
        return Fração.simplify(Fração(xnum, xden))
    
    def __str__(self):
        
        
  
        if self.den == 1:
            text__frac = "%d" %self.num
        
        else:
            text__frac = "%d/%d" %(self.num,self.den)
        
        return text__frac
    
    def __truediv__(self, other):
        
        novo__num = self.num * other.den
        novo__den = self.den * other.num
        
        f = Fração.simplify(Fração(novo__num, novo__den))
        
        return f

    
    def __pow__(self, expo):
        
        if type(expo) != int:
            
            raise ValueError("Expoente não inteiro")
        
        if expo>=0:
            
            novo__num = (self.num)**expo
            novo__den = (self.den)**expo
        
        else:
            
            novo__num = 1/(self.num)**expo
            novo__den = 1/(self.den)**expo
        
        f = Fração.simplify(Fração(novo__num, novo__den))
        
        return f
    
        
    def __eq__(self, other):
        
        prim__num = self.num  * other.den
        seg__num  = other.num * self.den
        
        return prim__num == seg__num
    
    def __lt__(self,other):
        
        prim__num = self.num  * other.den 
        seg__num  = other.num * self.den 
        
        return prim__num < seg__num
    
    
    def __le__(self, other):
        
        prim__num = self.num  * other.den 
        seg__num  = other.num * self.den 
        
        return prim__num <= seg__num
    
    def __gt__(self, other):
        
        prim__num = self.num  * other.den 
        seg__num  = other.num * self.den 
        
        return prim__num > seg__num
    
    def __ge__(self, other):
        
        prim__num = self.num  * other.den 
        seg__num  = other.num * self.den 
        
        return prim__num >= seg__num
    
    def __ne__(self, other):
        
        prim__num = self.num  * other.den 
        seg__num  = other.num * self.den 
        
        return prim__num != seg__num
        
    







