# lists are ordered data structure
a = [1,3,4,5,67]
print(a)
#Accessing any element
print(a[3])
#Slicing the lsit
print(a[1:4])
#adding an element to the list
a[0] = 98
print(a)
#replacing an element
a[1] = " "
print(a)

#List methods

#sorting the list
l1 = [2,6,7,1,74,89,43]
print(l1)
l1.sort()
print(l1)

#reverse the list

l1.reverse()
print(l1)

#Appending an element to the end

l1.append(23)
print(l1)

#inserting an element
l1.insert(1,254)      # inserts 254 and index 1
print(l1)

# popping an element usong the index

l1.pop(1)
print(l1)

# removing an element from the lsit

l1.remove(23)
print(l1)