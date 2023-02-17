# Convert an array to reduced form
array=[]

#Entering the array
enter=int(input("Enter number of elements: "))
for index0 in range(0,enter):
    element=int(input())
    array.append(element)
print("Original array: ",array)


# Duplicating and sorting an array
lengthOfFirstArray=len(array)
duplicateArray=[0]*lengthOfFirstArray
for index1 in range(0,lengthOfFirstArray,1):
    duplicateArray[index1]=array[index1]
duplicateArray.sort()
lengthOfDuplicateArray=len(duplicateArray)


#Reduced form
for index2 in range(0,lengthOfDuplicateArray,1):
    for index3 in range(0,lengthOfDuplicateArray,1):
        if (duplicateArray[index2]==array[index3]):
            array[index3] = index2
print("Original array reduced form: ",array)

