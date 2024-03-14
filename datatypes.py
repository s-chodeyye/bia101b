
#creation of array
array1 = [1,2,3,"thimphu",2.5]

#retrieving
element1= array1[0]
element2= array1[4]
lastElement = array1[-5]
print(element1)
print(element2)
print(lastElement)

#modifying elements
array1[0] = 10
print(array1)



#getting number of elements in an array
no_of_elements = len(array1)
print(no_of_elements)


#slicing
elements = array1[0:2]
print(elements)

#print elements
arr1 = [1,3]
arr2 = ['sonam','pema'] 
number_to_check = 2
result = number_to_check in arr1
print ('result is',result)
arr3 = arr1 + arr2
print(arr3)


arrVariable = [1,2,3]
arrVariable.append(4)
print(arrVariable) #1,2,3,4

#insert at a specific index
arrVariable.insert(1,10)
arrVariable.sort()
print(arrVariable)


stackvar = []
#adding to stack
stackvar.append(4)
stackvar.append(2)
stackvar.append(9)
stackvar.append(4)
print('After appending', stackvar)
element = stackvar.pop()
print('After popping', stackvar)
print ('removed element:', stackvar)
