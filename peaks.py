"""
This function takes an array as input 
and return a list of indices where a "peak" occurs in the list.
A peak is an element that is greater than both its neighbors.
"""
def FindPeaks ( array ):
    indices = []
#this loop iterate through the array,
#starting from the second element, and checking if the current element
#is greater than its neighbors. if yes, add the index of this element to the list of peaks.
    for i in range (1, len(array)-1):
        if array[i] > array[i-1] and array[i] > array[i+1] :
            indices.append( i )
    return indices

array = []
size = int ( input ("Please enter the size of your array:") )
#if condition is needed here to check if the array contains less than 3 elements
#because a peak cannot exist in these cases
if size == 1 or size == 2 :
    indices_array = []
    print ("Tiny array, no peaks here!")
elif size == 0 :
    print ("Add a valid number")
else:
    for i in range ( size ):
        values = int ( input("Enter your values: ") )
        array.append( values )
    indices_array = FindPeaks ( array )
    print ("Lets find some peaks! Peaks in your array correspond to the indices",indices_array )
