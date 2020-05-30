#PROGRAM TO REVERSE ALPHABETS LEAVING SPECIAL CHARACTERS AT SAME POSITIONS
str1=input()#Reading the string
al=[]# Creating a list to store alphabets
sc={}#Creating a dictonary to store special characters.
c=0
# storing alphabets in a list
#storing special characters in dictonary along with their indexes
for i in str1:
    if(ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122):
        al.append(i)
    else:
        sc[c]=i #store the index as key because comparing indexes we can retrieve the spl characters
    c+=1
s=""#declaring an empty string

n=len(al)-1#Store the size of alphabets list.

for i in range(len(str1)):#Now to print the new string consider the loops iteration until old string size
    if i in sc.keys():#Checking whether the index is an index of spl char
        s=s+sc[i]# If it is an index add its value to string.
    else:
        s=s+al[n]#Now if the above cond fails the last char of alphabets list is appended 
        n-=1#Decrement n so as to get the characters from last to first
print(s)#finally print the String.
    
