""" 

    @Author: Likhitha S
    @Date: 16-09-2024 9:19
    @Last Modified by: Likhitha S
    @Last Modified time: 16-09-2024 9:19
    @Title:Write a programs to reverse a number

"""
# Leap Year : Yes or No

"""
    
    Description: 
        This function is used to check a given number is leap year.
    Parameters:
        num->It is used to take the user input as type integer
    return:
        It print the leap year or not.

"""


def main():
    num=int(input('Enter the year:'))
    if num%4==0 and num%100!=0 or num%400==0:
              print(num," It's a leap year!!")
    else: 
        print(num,"It's not a leap year ")

if __name__=="__main__":
    main()