import maya.cmds.cmds

my_number = 10
if (my_number == 10) :
     print " Wow, it's 10!"
     my_number = 9
elif (my_number == 9):
     print "I MADE IT TO 9"
     my_number = 13
elif (my_number < 0):
     print "Stop being so negative."
     my_number *= -1
else:
     print "Thats not right!"


     # LOOPS
import maya.cmds as cmds

sels = cmds.ls(sl=True)

for value in [1, 2, 3, 4, 5]:
     print value
     print value ** 2  # squared

     print"IHJATEIT"




import maya.cmds.cmds
sels = cmds.ls(sl=True)
for value in sels:
     print value









