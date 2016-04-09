#-*-coding:utf-8-*-
"""栈：是一种先进先出的数据结构，比如一叠书，得先拿上面一本才可以拿下面一本。"""

class Stack(object):
	def __init__(self):
		self._stack=[]

	def push(self,*value):
		for n in value:
			self._stack.append(n)

	def out(self):
		return self._stack.pop()

	def noempty(self):
		if(len(self._stack)!=0):
			return True
		else:
			return False

	def view(self):
		return self._stack

	def number(self):
		return len(self._stack)

# 我们可以利用栈来解决一个回文问题
# 可以正反读的就是回文，‘xyzyx’就是回文，而‘ahah’不是。
# 可以发现回文长度都是奇数，所以长度为偶数的都不是回文。
def decrypt(string):
	length = len(string)
	if length%2==0 :
		print('1.不是回文')
		return False
	else:
		mid = length/2# 计算中间元素的位置
		stack = Stack()
		for i in range(0,mid):# 将前mid个数据入栈，不包括mid位置的元素
			stack.push(string[i])
		for j in range(mid+1,length):# mid+1是跳过中间元素
			temp = stack.out()
			if(temp!=string[j]):
				print('2.不是回文')
				return False
		print('yes')# 不知道为什么我这里是中文就一直不输出，我以为是什么bug一直没找到，最后到处试了才发现这里被坑了
		return True

decrypt('ahtha')