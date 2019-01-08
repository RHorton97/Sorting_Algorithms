#Merge Sort
#Best Case: O(n log(n))
#Average Case: O(n log(n))
#Worst Case: O(n log(n))

def mergeSort(aList):
    '''Merge sort
       Takes an list of comparable values and sorts them using
       merge sort before returning them in a list'''
    if len(aList) <= 1:
        return aList

    #Splits the list in two
    midPoint = len(aList)//2
    list1 = aList[:midPoint]
    list2 = aList[midPoint:]

    #Sorts each half
    list1 = mergeSort(list1)
    list2 = mergeSort(list2)

    return merge(list1, list2) #Returns the sorted list

def merge(list1, list2):
    '''Merge function for MergeSort to call
       Merges two lists together into a single sorted list before
       returning that list'''
    output = list() #Creates list to store sorted values in
    i = 0 #Indexes to cycle through the lists
    j = 0

    #Loops through values until one list is completed
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            output.append(list1[i])
            i = i + 1
        else:
            output.append(list2[j])
            j = j + 1

    #Checks for leftover values in list1
    while i < len(list1): 
        output.append(list1[i]) 
        i = i + 1

    #Checks for leftover values in list2
    while j < len(list2): 
        output.append(list2[j]) 
        j = j + 1

    return output

if __name__ == "__main__":
    a = [4, 1, 8, 10, 3, 6]
    print("Unsorted:", a)
    a = mergeSort(a)
    print("Sorted:", a)
