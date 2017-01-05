class stack:

	def __init__(self): 
		self.stack = []

	def push(self, e):
		self.stack.append(e)

	def pop(self):
		if not self.empty():
			self.stack.pop(len(self.stack) - 1)
		else:
			print('Stack Empty')	

	def top(self):
		if not self.empty():
			return self.stack[-1]
		return 'Stack is Empty'	

	def empty(self):
		if(len(self.stack) == 0):
			return 'Stack is Empty'

	def length(self):
		return len(self.stack)	

s = stack()
print(s.empty())
s.push(1)
s.push(2)
s.push(3)

s.pop()
s.pop()
print(s.length())