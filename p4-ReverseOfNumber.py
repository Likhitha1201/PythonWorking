""" 

        @Author: Likhitha S
        @Date: 14-09-2024 9:19
        @Last Modified by: Likhitha S
        @Last Modified time: 14-09-2024 9:19
        @Title: Write a python program to reverse a given number

"""

# Reverse number : 112 -->211

"""

        Description: 
            This function is used to return the reverse of a given number.
        Parameters:
            (num)It is used to take the input from the user of type integer
        return:
            It print the reverse of the given it.
        
"""


def main():
    num= int(input("Enter the number which has to be reversed:"))
    rev=0

    while num>0:
      n=num%10
      rev=rev*10+n
      num=num//10
   
    print(rev) 
    
main()