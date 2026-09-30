class Pila:
    def __init__(self):self.items = []
    def apilar(self,x):self.items.append(x)
    def desapilar(self):
        if self.vacia():return None
        return self.items.pop()
    def cima(self):return None if self.vacia() else self.items[-1]
    def vacia(self):return len(self.items) == 0

def balanceados(s):
    p=Pila(); pares={')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{': p.apilar(c)
        elif c in ')]}':
            if p.desapilar() != pares[c]: return False
    return p.vacia()

print(balanceados("()"))
print(balanceados("(a[b]{c})"))
print(balanceados("([)]"))
print(balanceados("((())"))
print(balanceados("{a}[b](c)"))
print(balanceados(""))

