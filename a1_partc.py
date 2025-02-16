# Copy over your a1_partc.py file here
#    Main Author(s): 
#    Main Reviewer(s):



class Stack:


	def __init__(self, cap = 10):
		self.cap =cap
		self.items = [None] * cap
		self.last_index = 0
		

	def capacity(self):
		return self.cap

	def resize(self):

		self.cap *= 2
		new_list = [None] * self.cap
		for i in range(0,self.__len__()):
			new_list[i] = self.items[i] 
			self.items = new_list

	def push(self, data):

		if self.last_index == self.cap:
			self.resize()

		self.items[self.last_index] = data
		self.last_index += 1
		
		

	def pop(self):
		if self.is_empty():
			raise IndexError('pop() used on empty stack')
		self.last_index -=1 
		value = self.items[self.last_index]
		self.items[self.last_index] = None
		return value

	def get_top(self):
		return self.items[self.last_index-1]

	def is_empty(self):
		if self.last_index == 0:
			return True
		return False

	def __len__(self):
		return self.last_index


class Queue:


	def __init__(self, cap = 10):

		self.cap = cap
		self.items = [None]*cap
		self.front = 0
		self.back = 0
		

	def capacity(self):
		return self.cap
	

	def resize(self):
		self.cap *=2
		new_list = [None] * self.cap
		n = 0
		for i in self.items:
			new_list[n] = i
			n += 1
		self.items = new_list


	def enqueue(self, data):

		if self.back == self.cap:
			self.resize()
			

		self.items[self.back] = data
		self.back+=1

	def dequeue(self):

		if self.is_empty():
			raise IndexError('dequeue() used on empty queue')
		else:
			value = self.items[self.front]
			self.items = self.items[1:] + [None]
			self.back -= 1
			return value

	def get_front(self):

		return self.items[self.front]

	def is_empty(self):

		if self.front == self.back :
			return True
		return False

	def __len__(self):

		if self.is_empty():
			return 0
		else:
			return self.back



class Deque:

	def __init__(self, cap=10):

		self.cap = cap
		self.items = [None] * cap
		self.front = 0
		self.back = 0
		self.len = 0



	def capacity(self):
		return self.cap

	def resize(self):
		self.cap *=2
		new_list = [None] * self.cap
		n = 0
		for i in self.items:
			new_list[n] = i
			n += 1
		self.items = new_list

	def push_front(self, data):

		if self.len == self.cap:
			self.resize()

		self.items = [data] + self.items

		self.back += 1

		self.len += 1


	def push_back(self, data):

		if self.len == self.cap:
			self.resize()
			

		self.items[self.back] = data
		self.back += 1
		self.len += 1

	def pop_front(self):
		
		if self.is_empty():
			raise IndexError('pop_front() used on empty deque')
		else:
			value = self.items[self.front]
			self.items = self.items[1:] + [None]
			self.back -= 1
			self.len -= 1
			return value

	def pop_back(self):

		if self.is_empty():
			raise IndexError('pop_back() used on empty deque')
		else:
			self.back -= 1
			value = self.items[self.back]
			self.items[self.back] = None
			self.len -= 1
			return value

	def get_front(self):
		return self.items[self.front]

	def get_back(self):
		return self.items[self.back-1]

	def is_empty(self):
		if self.len == 0:
			return True
		return False


	def __len__(self):
		if self.is_empty():
			return 0
		else:
			return self.len




	def __getitem__(self, k):
		
		if k >= self.back:
			raise IndexError('Index out of range')
		else:
			return self.items[k]
