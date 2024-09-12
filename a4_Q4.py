# Family name: Kairly Tawk 
# Student number: 300298495
# Course: IT1 1120 
# Assignment Number 4, Part 1


def read_raw(file):
    '''str->list of str
    Returns a list of strings that was stored in a file.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str

    The functions takes as input a list of characters.
    It returns a new list containing the same characters as l except that
    one of each characters that appears odd number of times in l is removed
    and all the * characters are removed

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''   
 
    clean_board = []
    odd_element=[]
    for i in range(len(l)):
        if l[i] != '*':
            count = l.count(l[i])
            clean_board.append(l[i])
            if l[i] not in odd_element and count%2!=0:
                odd_element.append(l[i])              
    l=clean_board.copy()
    for i in range(len(clean_board)):
        if clean_board[i] in odd_element:
            l.remove(clean_board[i])
            odd_element.remove(clean_board[i])          
    clean_board=l   
    clean_board.sort()
    return clean_board
    


def is_rigorous(l):
    '''list of str->bool
    Returns True if every character in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: You may assume that every element in the list appears even number of times
    (i.e. that the list is clean-up by clean_up function)

    >>> is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>> is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    #YOUR CODE GOES HERE
    
    if len(l)==0:
        return True
    for item in l:
        if l.count(item)!=2:
            return False
    return True

    
#main
file=input("Enter the name of the file: ")
file=file.strip()
b=read_raw(file)
print("\nBefore clean-up:\n", b)
b=clean_up(b)
print("\nAfter clean-up:\n", b)
if is_rigorous(b):
    print("\nThis list is now rigorous; it has no * and it has "+str(len(b))+" characters.")
else:
    print("\nThis list has no * but is not rigorous and it has "+str(len(b))+" characters.")
     
