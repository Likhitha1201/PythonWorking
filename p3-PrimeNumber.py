""" 
@Author: Likhitha S
@Date: 14-09-2024 9:19
@Last Modified by: Likhitha S
@Last Modified time: 14-09-2024 9:19
@Title: Listing prime number
"""

# Prime number : 2, 3, 5, 7, 11.........

"""
    Description: 
        This function is used to calculate the prime number.
    Parameters:
        num: It is used to take the user input as type integer
        It print's the group of prime number with in given num.
"""
num = int(input("Enter the number:"))
for i in range(2,num):
    if num%i==0:
       print('given ',num,' is not a prime number') 
       break
else:
   print(num,' is a prime number')