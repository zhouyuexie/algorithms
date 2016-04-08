#-*-coding:utf-8-*-

from datetime import datetime

a=[3,5,1,5,7,3,7,2,9,0,45,72,345,231,8,25,17,78,1,9,99,7,233]

# 相当于玩扑克牌
def insert_sort(a):
	for i in range(1,len(a)):#从桌上一个个的拿牌
		while(a[i]<a[i-1] and i>0):#和手上的牌一个个比较，插入到合适的位置
		#如果需要改变排序方式可以直接修改a[i]>a[i-1]
			key = a[i]
			a[i] = a[i-1]
			a[i-1] = key
			i = i-1
	return a

print(insert_sort(a))