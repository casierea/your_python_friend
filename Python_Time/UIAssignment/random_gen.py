
import maya.cmds as cmds
sels = cmds.ls(sl=True) #list of values
duplicates = 3

for value in range (duplicates): #quickest way to do it.
        print value

for value in 'My String': #print each value out 1 by 1
    print value



    #use the size
#len(sels)

#To do
import maya.cmds as cmds
sels = cmds.ls(sl=True) #list of value
duplicates = 3

list_length = len(sels)
for value in range(list_length):
    #for value in range(len(sels)): This is nesting. Find len of sel= (sel is the maya commad)
    #deepest command 1st.  find 5, then substitue range for 5.
    print value

#Now he has it showing code from above nested.

import maya.cmds as cmds
duplicates = 3
for value in range (len(cmds.ls(sl=True))):
    print value

#while
number = 0
while (number < 10):
    print number
    number += 1

###functions###

#def # define

import maya.cmds as cmds
def add(value1=3, value2=5): #arguments
    sum = 0
    sum = value1 + value2
    return sum
    add(3, 5)

#add('hello, str(3')

import random

random.randrange(5,9)