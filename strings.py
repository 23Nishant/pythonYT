#simple string
a = 'Nishant Tomar'
print(a)
#using double quotes to use single quote in the sentence
b = "Nishant's Program"
print(b)
# triple quotes lets us print multiline strings
c = '''I am
a python programmer'''
print(c)

#first index is included but the last index is not included
print(a[1:5])
print(a[3])
print(a + " " + b)
print(a[-3:-1])

#Slicing with skip value

print(a[1:7:2])
#It prints the alphabets fron 1 to 6 index while printing every 2nd alphabet

print(a[0::2])
#prints every second alphabet from index 0 to the end

#String Functions

print(len(a))
print(a.endswith('mar'))
print(a.endswith('mad'))
print(a.count('n'))
print(a.capitalize())  #first character is capitalized
print(a.find('mar'))
print(a.replace("Tomar" , "dad"))

#Escape sequencr \n
print('Nishant \nTomar')

#to print \ we have to type \\
print('Nishant\\s Program')



