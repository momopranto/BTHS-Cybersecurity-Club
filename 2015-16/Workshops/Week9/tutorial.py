#assigning an string variable
x = "starbucks"     #notice no semi-colons
#assigning a integer variable
x = 4  #note python has dynamic variable types
#the previous value of x, "starbucks", has now been overwritten

#arithmetic operations
print x + 1  #output: 5
x = x - 1    #the result of x-1 was stored back in x
print x      #output: 3
print x * 0  #output: 0
print x / 1  #output: 3

#store data in a list
myList = [1, 3, 3, 7]
#add something to a list
myList.append(0)  #myList now contains [1, 3, 3, 7]
#access specific things in a list
print myList[2]   #prints the 3rd item in the list (in programming everything starts at 0)

#if statements if the condition returns a boolean value of True
#boolean operators generally compare two things using the following operators (<, >, <=, >=, ==, !=)
if (1 < 10):    #don't forget the colon ":"!
    print True

#else statements can be used to handle alternate cases
if (4*5 == 20):   #"==" checks that two things are equal
    print True
else:             #if the above condition is false this will execute
    print False


#while loop
n = 0
while(n < 10):
    n = n + 1     #this will repeat until n is no longer less than 10
print n           #output: 10

#for loop
sum = 0
for i in range(5):
    sum = sum + 2   #this will add 2 to the sum 5 times
print sum           #output: 10
