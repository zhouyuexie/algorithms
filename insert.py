#-*-coding:utf-8-*-
'插入排序：将无序的数据序列插入到一个有序的数据序列，要求插入后仍然有序'

from datetime import datetime
import random

# 生成一个随机数组
array = []
for x in range(0,10000):
	array.append(random.randint(0,100000))

# 相当于玩扑克牌，从桌上一个个的拿牌，和手上的牌一个个比较，插入到合适的位置
# 不过下面的算法是当前序列（数组）排序，没有利用其他数组
def insert_sort(a):
	for i in range(1,len(a)):# 从数组第二个元素开始，然后向右移动
		while(a[i]<a[i-1] and i>0):# 当前元素和左边全部元素比较，插入到合适的位置
		#如果需要改变排序方式可以直接修改上面a[i]>a[i-1]
			key = a[i]# 交换两个元素
			a[i] = a[i-1]# 交换两个元素
			a[i-1] = key# 交换两个元素
			i = i-1# 继续和下一个元素比较
	return a

start = datetime.now().second# 开始时间
print(insert_sort(array))
end = datetime.now().second# 结束时间

print float(end-start)#运行经历时间
