""" 
@Author: Likhitha S
@Date: 14-09-2024 9:19
@Last Modified by: Likhitha S
@Last Modified time: 14-09-2024 9:19
@Title: checking perfect number or not
"""

# Perfect numbers : 6, 28, 496, 8128....................

"""
    Description: 
        This function is used to calculate the fibonacci series.
    Parameters:
        num: It is used to take the user input as type integer
        It print's wheather the given number is perfect num or not.
"""
num=int(input('Enter the number:'))
sum=0
for i in range(1,num):
    if i<num:
        if num%i==0:
            sum=sum+i
            
if sum==num:
    print(num,' is perfect number!!')
else:
    print(num,' is not a perfect number?? ')