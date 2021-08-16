
#Ques 6.Write a Python program to construct the following pattern, using a nested for loop.
 #         *       (here # hash is comment)
 #         *       (here # hash is comment)
 #         *        (here # hash is comment)
 #         *      (here # hash is comment)
 #         *       (here # hash is comment)
print('Pattern Print')

n=6
for i in range(n):
    for j in range(i):
        print('*')
        break