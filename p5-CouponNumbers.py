""" 

        @Author: Likhitha S
        @Date: 16-09-2024 9:19
        @Last Modified by: Likhitha S
        @Last Modified time: 16-09-2024 9:19
        @Title: Write a python program to generate n distinct coupon number and search wheather they own or not

"""

# Reverse number : 112 -->211

"""

        Description: 
            This function is used to check there luck factor in coupon.
        Parameters:
            (coupon)It is used to take the coupon input from the user of type integer.
        return:
            It prevents wheather they own or not with the relevent messages.
        
"""

from random import randint
coupon =int(input('Enter the 4 digit coupan number: '))
generated=1
res=0
i=0
while generated<=10:
    if coupon ==print(randint(0,9),randint(0,9),randint(0,9),randint(0,9)):
        print('Wow Congrats!!!, You Won this!!!')
        generated=generated+1
    else:
        print('Sorry!! Better Luck Next time!!!!')
        generated=generated+1
