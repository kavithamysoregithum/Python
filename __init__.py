a=557
b=11
c=b-a
d=a+b
f1=b/a
e=b % a 
print("c= b-a=",c,"\nd= a+b=",d,"\ne= b%a=",e, "\nf= b/a=",f1)
# Power operations
print("2 to the power of 3 =", 2 ** 3)
print("Type of variable a is =",type(a))
a=5.5
print("Dynamic typing a is now decimal number = ",a)
print("Type of variable a is =",type(a))
#Length of string
lengtHstring = "This is a string"
print("The length of the string = ",len(lengtHstring))
print("Printing the 8th character in the string = ", lengtHstring[8].upper())
print("Printing the 8th character using negative indexing = ",lengtHstring[-8].upper())
print("Printing upto 8th character string[:9] = ",lengtHstring[:9].upper())
print("Printing from 8th character string[8:] = ",lengtHstring[8:].upper())
print("Printing alternative characters string[::2] = ",lengtHstring[::2].upper())
print("Printing split words = ",lengtHstring.upper().split())
print("Format string {Value:width.precision f}".upper())
print("Adding {} {} {}".format('name3','name1','name2'))
print("Adding in the right format {1} {2} {0}".format('name3','name1','name2'))
print("Adding in the right format using key words {On} {Tw} {Th}".format(Th='name3',On='name1',Tw='name2'))
print("Print width and precision {numb:1.2f}".format(numb=f1))
print("The value of b = {}".format(b))
