import maya.cmds as cmds
sels = cmds.ls(sl=True)
duplicates = 3


for value in sels:
    print value

#run a for looop 5 times

range(5)

for value in range(5):
    print value
    # range can have a min and max

for value in range (duplicates): #quickest way to do it.
        print value
def add(value1=3, value2=5): #arguments
    sum = 0
    sum = value1 + value2
    return sum
    add(3, 5)