#-*-coding:utf-8-*-
'插入排序：将无序的数据序列插入到一个有序的数据序列，要求插入后仍然有序'

from datetime import datetime

a=[3,5,1,5,7,3,7,2,9,0,45,72,345,231,8,25,17,78,1,9,99,7,233]

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

print(insert_sort(a))