'''
Write a Python program to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using 
a) Insertion sort
b) Shell sort and display top five scores
'''
# Function to take student percentage:------------------------------------------------

def createArray(n):
    array = []
    for i in range(n):
        percentage = float(input(f"Enter percentage of student {i+1}: "))
        array.append(percentage)
    return array

# Intertion Sort ----------------------------------------------------------->>>

def intertionSort(array):
    n = len(array)-1
    for i in range(n):
        j = i+1
        if array[i]>array[j]:
            array[i], array[j] = array[j], array[i]
        k = i
        while k>=0 and array[k-1]>array[k]:
            if (k-1)<0:
                break
            elif array[k]<array[k-1]:
                array[k], array[k-1] = array[k-1], array[k]
                k -= 1
            else:
                k -= 1
    return array

# shell sort -------------------------------------------------------------------------

def shellSort(arr):
    gap = len(arr) // 2 
    while gap > 0:
        i = 0
        j = gap
        while j < len(arr):
     
            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
             
            i += 1
            j += 1
            k = i
            while k - gap > -1:
                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                k -= 1
        gap //= 2
    return array 


# Main program start from here -----------------------------------------------------

n = int(input("Enter total number of students value: "))
array = createArray(n)
print("Sorted students array using intertion sort: ", intertionSort(array))
mini = len(array)-6
maxi = len(array)-1
index = 1
array = shellSort(array)
print("---------------------Top scorer using shell sort-------------------------\n")
for i in range(maxi, mini, -1):
    if i>=0:
        print(f"Topper No. {index}", array[i],"\n")
    index+=1   
                

