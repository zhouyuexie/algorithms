#-*-coding:utf-8-*-
'快速排序：是对冒泡排序的一种改进。'
from datetime import datetime
import random

# 生成一个随机数组
array = []
for x in range(0,10000):
	array.append(random.randint(0,100000))

# 快速排序
def quicksort(array,low,hign):
	i = low
	j = hign
	if(i>=j):
		return array# 数组只剩一个元素或者没有元素
	keyvalue = array[low]# 基准数
	while(i!=j):
		while(array[j]>=keyvalue and i<j):
			j = j-1# 没有找到比基准数小的元素就一直找
		while(array[i]<=keyvalue and i<j):
			i = i+1# 没有找到比基准数大的元素就一直找

		if(i<j):# 交换i，j两个位置的元素
			t = array[i]
			array[i] = array[j]
			array[j] = t
	array[low] = array[i]# 将基数换到i=j的位置
	array[i] = keyvalue# 将i=j位置的元素换到基数位置
	quicksort(array,low,i-1)# 递归运算左边数组，i=j的元素已经排好
	quicksort(array,j+1,hign)# 递归运算右边数组
	return array

start = datetime.now().microsecond# 开始时间
print(quicksort(array,0,len(array)-1)[:100])# 输出前一百个
end = datetime.now().microsecond# 结束时间

print float(end-start)/1000000#运行经历时间
