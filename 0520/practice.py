#
# str = "aabbcc"
# print (str.upper( ))
# # AABBCC
# def haha(x,y):
#     if x==y:
#         return x,y
#
# print(haha(1,1))

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}",end=' ')
#     print(' ')

# 使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）
#
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法

a=[1,7,4,89,34,2]
#print(a.index(1))
for i in range(len(a)-1):
    #print(i)
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
