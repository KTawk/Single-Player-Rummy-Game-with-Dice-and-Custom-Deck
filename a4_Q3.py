# Family name: Kairly Tawk 
# Student number: 300298495
# Course: IT1 1120 
# Assignment Number 4, Part 1


def longest_run(lst):
    '''
    (list) --> int
    Returns the length of the longest run
    '''
    
    maxx = 1
    for i in range(len(lst)-1):
        count = 1
        while i < len(lst)-1  and lst[i] == lst[i+1]:
            count += 1
            i += 1
        #count += 1
        if count > 1 and count>maxx:
            maxx = count
    return maxx

lst = input("Please input a list of numbers separated by space: ").strip().split()

accumulator = []
for item in lst:
    accumulator.append(float(item))

if len(lst) == 1:
    print('1')
elif len(lst)<1:
    print('0')
else:
    print(longest_run(accumulator))
