#Exemplo de pilha optimizada
class Pilha:
	def __init__(self):
		self.pilha = []
		self.pilha_len = 0
	def push(self, n): #Adiciona elemento no final da lista
		self.pilha.append(n)
		self.pilha_len += 1
	def pop(self): #Remove elemento no final da lista
		if not self.empty():
			self.pilha.pop(self.pilha_len - 1)
			self.pilha_len -= 1
	def top(self): #Mostra elemento do topo da lista
		if not self.empty():
			return self.pilha[-1]
		return None
	def empty(self): #Ver se a lista estar vazia
		if self.pilha_len  == 0:
			return True
		return False
	def length(self): #Mostra o tamanho da lista
		return self.pilha_len

p=Pilha()
p.push(1)
p.push(2)
p.push(3)
p.pop()
print(p.top())
print(p.length())

