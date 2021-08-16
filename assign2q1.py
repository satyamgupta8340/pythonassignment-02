# Ques 1. Write a Python program to remove duplicates from a list.

l1=[10,5,8,6,5,4,2,2,8,10,11]
result=[]
for i in l1:
    if i not in result:
        result.append(i)
    
print(result)