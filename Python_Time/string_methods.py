import maya.cmds as cmds
# the replace() replaces a string with another string
# strings are also a list of characters
my_string = 'the is my string'

my_string = 'Leg_##_Jnt'

if '#' in my_string:  # This doesnt says where. but does say it is in the string
    print 'yes'
else:
    print 'no'


my_string = 'Leg_##_Jnt'
('Leg_','#', '_Jnt')
print my_string.partition('#')  #we want it to look for this character #

# Have to verify that the # character exists and how many. And make sure they are next to eachother




#Leg_##_Jnt
my_string = 'Leg_##_Jnt'
num_of_hash = 3
txt = str(1) #cast number into string value and assign it
#x = txt.zfill(num_of_hash)
x = str(1).zfill(num_of_hash)
print(x)