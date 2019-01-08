#Bubble Sort
#Best Case: O(n)
#Average Case: O(n^2)
#Worst Case: O(n^2)

def bubbleSort(aList):
    '''Bubble sort
       Takes an list of comparable values and sorts them using
       bubble sort before returning them in a list'''
    swap = True #Variable to track if a swap has happened
    
    while swap:
        swap = False #Breaks loop if no swap happens on any given pass
        for i in range(0, len(aList)-1): #Loops through list
            j = i + 1 #Sets second value of pair
            if aList[i] > aList[j]: #If values aren't ordered, swap them
                swap = True #Marks that a swap has happened on this pass
                iVal = aList[i]
                jVal = aList[j]
                aList[i] = jVal
                aList[j] = iVal

    return aList

if __name__ == "__main__":
    a = [4, 1, 8, 10, 3, 6]
    print("Unsorted:", a)
    a = bubbleSort(a)
    print("Sorted:", a)
