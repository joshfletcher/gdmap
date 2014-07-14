def hail_stone(l,h):
    '''
    
    
    '''
    length = 0
    max_length = 0 ##

    for n in range(l,h):
        print "Sequence #:", n
        seq = [] ##
        while n != 1:
            print n,
            seq.append(n)  ##
            if n % 2 == 0:
               n = n / 2
               length = length + 1
            else:
                n = (n * 3) + 1
                length = length + 1
            if n == 1:
                print n
                seq.append(n) ##
                length = length + 1
        print "The sequence above contains", length, "numbers"

        if length > max_length:  ##
            max_length = length  ##
            max_seq = seq[:]     ##

    length = 0

    print 'max length: ', max_length ## same as len(max_seq)
    print 'max seq: ', max_seq       ##



hail_stone(1,10)


''' Understand the power of functions (machines) in D.R.Y  - Don't repeat yourself '''

def hello(a_name,age):
    print "Hello from ", a_name, ", and love being ", age, "years old"
    
    

my_name="Joshua"


#hello(my_name, 11)    


# for n in range(0,12):
#     hello(my_name,n)
    
