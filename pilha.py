#Exemplo de pilha
class Pilha:
	def __init__(self):
		self.pilha = []
	def push(self, n): #Adiciona elemento no final da lista
		self.pilha.append(n)
	def pop(self): #Remove elemento no final da lista
		if not self.empty():
			self.pilha.pop(len(self.pilha) - 1)
	def top(self): #Mostra elemento do topo da lista
		if not self.empty():
			return self.pilha[-1]
		return None
	def empty(self): #Ver se a lista estar vazia
		if (len(self.pilha) == 0):
			return True
		return False
	def length(self): #Mostra o tamanho da lista
		return len(self.pilha)

p=Pilha()
p.push(1)
p.push(2)
p.push(3)
p.pop()
print(p.top())
print(p.length())
