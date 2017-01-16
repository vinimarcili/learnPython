class stack:

	def __init__(self): 
		self.stack = []
		self.len_stack = 0

	def push(self, e):
		self.stack.append(e)
		self.len_stack += 1

	def pop(self):
		if not self.empty():
			self.stack.pop(self.len_stack - 1)
			self.len_stack -= 1
		else:
			print('Stack Empty')	

	def top(self):
		if not self.empty():
			return self.stack[-1]
		return 'Stack is Empty'	

	def empty(self):
		if self.len_stack == 0:
			return 'Stack is Empty'
		return False	

	def length(self):
		return self.len_stack	

s = stack()
print(s.empty())
s.push(1)
s.push(2)
s.push(3)
print(s.empty())
s.pop()
s.pop()
print(s.length())