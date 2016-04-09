#-*-coding:utf-8-*-
'归并算法：将已有序的子序列合并得到完全有序的序列。先使每个子序列有序，再使子序列段间有序'

from datetime import datetime
import random

# 生成一个随机数组
array = []
for x in range(0,10000):
    array.append(random.randint(0,100000))

# 这是直接合并两个‘有序’数组的算法
def merge(left,right):
    c=[]
    i=j=0
    while(i<len(left) and j<len(right)):# 将每个数组的元素相比较
        if left[i]<right[j]:# 改变这里大小可以改变排序
            c.append(left[i])# 将合适的数组增加到c数组中
            i=i+1
        else:
            c.append(right[j])# 将合适的数组增加到c数组中
            j=j+1
    # 下面两个while循环是防止两个数组相等而设置的，
    # 把多出来的数组元素直接加到c数组中
    while(i<len(left)):
        c.append(left[i])# 将剩下的元素增加到c数组中
        i=i+1
    while(j<len(right)):
        c.append(right[j])# 将剩下的元素增加到c数组中
        j=j+1
    return c

# 拆分一个数组然后合并
def mergesort(array):
	if(len(array)<=1):# 拆分到只有一个的时候返回，相当于已经排序好了
		return array
	mid = int(len(array)/2)# 获取数组中间下标
	left = mergesort(array[:mid])# 切片操作，左数组
	right = mergesort(array[mid:])# 切片操作，右数组
	return merge(left,right)

start = datetime.now().microsecond# 开始时间
print(mergesort(array))
end = datetime.now().microsecond# 结束时间

print float(end-start)/1000000#运行经历时间
