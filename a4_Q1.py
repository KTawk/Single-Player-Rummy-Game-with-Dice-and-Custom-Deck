# Family name: Kairly Tawk 
# Student number: 300298495
# Course: IT1 1120 
# Assignment Number 4, Part 1


# Question 1:

def number_divisible(lst, n):
    '''
    (list, int) --> int
    Returns the number of elements in the list that are divisible by n.
    '''
    count=0
    for item in lst:
        if item%n==0:
            count+=1
    return count


       
lst = input("Please input a list of numbers separated by space: ").strip().split()
n = int(input("Please input an integer for n: ").strip())

accumulator = []
for item in lst:
    accumulator.append(int(item))  
    
print("The number of elements divisible by",n,"is", number_divisible(accumulator, n))

