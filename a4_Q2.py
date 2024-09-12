# Family name: Kairly Tawk 
# Student number: 300298495
# Course: IT1 1120 
# Assignment Number 4, Part 1

# Question 2

def two_length_run(lst):
    '''(lst) --> bool
    Takes a list of numbers as input parameter and returns True
    if the given list has at least one run and False otherwise.
    '''
    if len(lst)<2:
        return False

    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False
        




lst = input("Please input a list of numbers separated by space: ").strip().split()

accumulator = []
for item in lst:
    if len(item)==1:
        accumulator.append(int(item))
    elif len(item)>1:
        accumulator.append(float(item))        

print(two_length_run(accumulator))
