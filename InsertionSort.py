#Insertion Sort
#Best Case: O(n)
#Average Case: O(n^2)
#Worst Case: O(n^2)

def insertionSort(aList):
    '''Insertion Sort
       Takes an list of comparable values and sorts them using
       insertion sort before returning them in a list'''
    for i in range(1, len(aList)):
        current = aList[i] #Select the item and make a copy

        j = i - 1 #Index of the previous item in the list

        #Runs while index is greater than or equal to 0 and the value at the
        #index is greater than the current value
        while j >= 0 and aList[j] > current:
            aList[j+1] = aList[j] #Moves the larger value up a position
            j = j - 1 #Sets the index one lower

        #Once loop is finished the current item is reinserted into the list
        #at the correct position
        aList[j+1] = current

    return aList

if __name__ == "__main__":
    a = [4, 1, 8, 10, 3, 6]
    print("Unsorted:", a)
    a = insertionSort(a)
    print("Sorted:", a)
