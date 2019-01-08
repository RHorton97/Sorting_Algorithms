#Selection Sort

def selectionSort(unsorted):
    '''Selection sort
       Takes an list of comparable values and sorts them using
       selction sort before returning them in a list'''
    
    sortedList = list()
    while unsorted != []: #Cycles through the unsorted list
        small = None
        for item in unsorted: #Finds the smallest item in the unsorted list
            if small == None:
                small = item
            else:
                if item < small:
                    small = item
                    
        sortedList.append(small) #Moves smallest item to sorted list
        index = unsorted.index(small) #Uses index to prevent duplicate deletion
        unsorted.pop(index) #Removes smallest item from unsorted list

    return sortedList

if __name__ == "__main__":
    a = [4, 1, 8, 10, 3, 6]
    print("Unsorted:", a)
    a = selectionSort(a)
    print("Sorted:", a)
