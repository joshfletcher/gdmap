'''

Start with any positive integer (an initial seed) and obtain a sequence of numbers by following these rules.

1. If the current number is even, divide it by two; else if it is odd, multiply it by three and add one. 
2. Repeat.

'''


''' YOur job is to add comments.  When you encounter a bug, read the error message '''
def simple_stone(n, logging=False):

    stone_list=[n]
    stone=None  
    while (stone_list[-1] != 1):  # returns true or false
       
        # Use the modulus operator to test whether the number is odd or even
        if (n % 2) == 0.0:
            stone = n / 2
        else:
            stone = (n * 3) + 1

        stone_list.append(stone)
        n = stone_list[-1]
        #End of while loop
        if logging:
            print "I'm doine with just one number,", stone, " I may need to contiue, the while loop logic will figure it out"
    print "I'm done"
    return stone_list
    

   
print simple_stone(2188, logging=True)
print simple_stone(218800, logging=True)
print simple_stone(21880002, logging=True)


