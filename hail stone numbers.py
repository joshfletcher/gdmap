def hail_stone_numbers(lo,hi):
	length=0
for n in range(lo,hi):
    print "Number:", n
    while n != 1:
        print n,
        if n % 2 == 0:
           n = n / 2
           length = length + 1
        else:
            n = (n * 3) + 1
            length = length + 1
        if n == 1:
            print n
            length = length + 1
    print "The sequence above contains", length, "numbers"
