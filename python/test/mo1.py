# 1.Create a Folder named "test" 
# 2.inside "test" create a module mo1.py 
# 3.inside mo1 write a logic to print all even numbers 
# 4.inside "test" create ipynb file call mo1 from jupyter notebook 
# 5.while calling this module take input from user..user can input any type of data string,special char..etc 
# 6.try to handle all the edge cases
# 7.try to log all the errors using logging  

import mod
import logging as lg

lg.basicConfig(filename = 'even.log', level=lg.INFO, format = '%(asctime)s %(message)s')

while True:
    try:
        inp = int(input('Enter the value - '))
        