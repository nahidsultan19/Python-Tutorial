class generate_number:


	def __init__(self, min, max):
		self.min = min
		self.max = max


	def __iter__(self):
		return self


	def __next__(self):
		if self.min > self.max:
			raise StopIteration
		else:
			self.min +=1
			return self.min -1

numbers = generate_number(10,50)
numbers.__next__()

for i in numbers:
	print(i)