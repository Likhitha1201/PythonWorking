""" 
@Author: Likhitha S
@Date: 15-09-2024 9:19
@Last Modified by: Likhitha S
@Last Modified time: 15-09-2024 9:19
@Title: flip a coin
"""
# Flip a coin --> 1-Head && 0-Tail

"""
    Description: 
        This function is used to calculate the chances of getting heads and tails.
    Parameters:
        num: It is used to take the random value by itself
        It print the random values and gives heads and tails.
"""

import random
side = random.randint(0,1)
if side==1:
    print('Head')
else:
    print('Tail')
if side<0.5:
    if side==0:
        print(side,((side+1)*100)//2)
else:  
    print(side,(side*100)//2)