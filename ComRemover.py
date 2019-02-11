import os

#getting the path of the file location
path=os.path.abspath(input("Give me the path of the file you want to clear from the comments: "))

print("Now we are checking your code! Please wait.....")
i=0
#var an array to insert in the lines without comments
no_com=[]
#open the file with the name code only to read
with open(path, 'r') as code:
    #checking in every line for not '#'
    #if the line  from '#' put it in an array
    no_com=[i for i in code if not i.startswith('#')]

#var i and j for while loops.
i=0
j=0
#pattern for '#' inside strings.
pattern_one='#\*.*?\*'
pattern_double="#\*.*?\*"
# 1st while loop to check every value of the array.
while i < len(no_com):
    # 2nd while loop to check letter by letter if they have the '#' in them.
    while j < len(no_com[i]):
        # 1st two if to check if the '#' is inside a string using the var pattern
        if pattern_double in no_com[i]:
            #the value does not change.
            no_com[i]=no_com[i]
        elif pattern_one in no_com[i]:
            no_com[i]=no_com[i]
        # 2nd if to check if '#' is after the code there is a comment
        elif '#' in no_com[i][j]:
            #spliting that specific value in the array in a new array.
            spliting=no_com[i].split('#')
            #the first value of the new array goes back to the specific value of the no_com array.
            no_com[i]=spliting[0]
        j+=1
    i+=1

print("Now we are are removing all comments! Please wait.....")
#open the file with the name new_code only to read only to write
with open(path,'w') as new_code:
    #using the for loop the programm writes the no_com array to the same file.
    for line in range(len(no_com)):
        #the new_code is using the write rule to write in the file the no_com[i] array and at the and add a new line
        new_code.write(no_com[line] + '\n')

print("Your code is free from comments! Enjoy :) ")
