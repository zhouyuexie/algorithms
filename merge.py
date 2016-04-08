#-*-coding:utf-8-*-
'归并算法：将已有序的子序列合并得到完全有序的序列。先使每个子序列有序，再使子序列段间有序'


a=[3,5,1,5,7,3,7,2,9,0,45,72,345,231,8,25,17,78,1,9,99,7,233]

# 这是直接合并两个‘有序’数组的算法
def merge(left,right):
    c=[]
    i=j=0
    while(i<len(left) and j<len(right)):# 将每个数组的元素相比较
        if left[i]<right[j]:# 改变这里大小可以改变排序
            c.append(left[i])
            i=i+1
        else:
            c.append(right[j])
            j=j+1
    # 下面两个while循环是防止两个数组相等而设置的，
    # 把多出来的数组元素直接加到c数组中
    while(i<len(left)):
        c.append(left[i])
        i=i+1
    while(j<len(right)):
        c.append(right[j])
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

print(mergesort(a))
