#-*-coding:utf-8-*-
"""队列：队列是一种先进先出的数据结构，比如排队，先来的先被服务。"""

class Queue():
	def __init__(self):# 初始化队列数据
		self._queue=[]# 使用数组存储数据

	def push(self,*value):# 增加数据
		for n in value:
			self._queue.append(n)

	def out(self):# 推出元素
		if(len(self._queue)==0):
			print("No data can use.")
			return False
		else:
			t = self._queue[0]
			del self._queue[0]
			return t

	def view(self):# 返回所有队列元素
		return self._queue

	def number(self):# 返回队列长度
		return len(self._queue)

# 使用队列解决一个解密问题，规则是：
# 先删除第一个元素，然后把第二个元素放到最后，再删除下一个元素...
# 一直到数组没有元素，然后输出这个解密后的数组
# 这个问题可以用队列来解决：
def decrypt(queue):
	a = []
	for i in range(0,queue.number()):
		result = queue.out()
		if(result):
			a.append(result)
			queue.push(queue.out())# 将推出的元素加到最后
	return a

queue = Queue()
queue.push(6,3,1,7,5,8,9,2,4)

print(decrypt(queue))