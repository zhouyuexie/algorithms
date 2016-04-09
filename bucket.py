#-*-coding:utf-8-*-
'桶排序是将数组分到有限数量的桶子里。假设数组全为正整数，最大的数为max，然后创建一个容量为max的桶，数组里的元素的值代表桶的位置，桶存储的是含当前下标大小值的元素‘个数’。'

from datetime import datetime
import random

# 生成一个随机数组
array = []
for x in range(0,10000):
	array.append(random.randint(0,100000))

def bucketsort(array):
	bucket = []
	result = []
	for i in range(0,max(array)+1):# 找到数组中最大的值
		bucket.append(0)# 创建一个大小为345的桶

	for j in array:# 循环数组里的元素
		bucket[j] = bucket[j]+1# 找到相应的位置自增1，bucket里的元素大小代表了含有多少个下标大小的元素，比如bucket[45]，值为2,则代表了数组a中45的元素有2个

	# 然后循环输出bucket中的元素，如果元素为0则跳过
	for i in range(0,len(bucket)):
		if(bucket[i]!=0):
			for j in range(0,bucket[i]):
				result.append(i)

	return result

start = datetime.now().microsecond# 开始时间
print(bucketsort(array))
end = datetime.now().microsecond# 结束时间

print float(end-start)/1000000#运行经历时间