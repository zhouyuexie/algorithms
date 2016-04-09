#-*-coding:utf-8-*-
'冒泡排序：非常简单的一个排序方式。'

from datetime import datetime
import random

# 生成一个随机数组
array = []
for x in range(0,10000):
	array.append(random.randint(0,100000))

def bubblesort(array):
	for i in range(0,len(array)-1):
		for j in range(0,len(array)-1):
			if(array[j]>array[j+1]):
				t = array[j]
				array[j] = array[j+1]
				array[j+1] = t
	return array

start = datetime.now().second# 开始时间
print(bubblesort(array))# 输出前一百个
end = datetime.now().second# 结束时间

print float(end-start)#运行经历时间