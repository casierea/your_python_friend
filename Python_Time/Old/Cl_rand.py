import maya.cmds as cmds
import random
#define a function
#   args: num of duplicate, minX, maxX, minY, maxY, minZ, maxZ
#get current selection and loop through each item
# for each item:
# duplicate the item
#   generate random numbers between [minX, maxX, minY, maxY, minZ, maxZ]
#   nmove the duplicate to the random location
#   store all duplicates into a list

# select all of the duplicates
# return all duplicates


def random_placement_generator(num_of_duplicates, min_x, max_x, min_y, max_y, min_z, max_z):
    """
    duplicates selected objects and places randomly throughout scene based on range

    Args:
        num_of_duplciates::number
            Specify number of duplicates to be made
        min_x::number
            Mininum x range

        :param num_of_duplicates:
        :param min_x:
        :param max_x:
        :param min_y:
        :param max_y:
        :param min_z:
        :param max_z:

    :Return:
        all_dups::string[]
            List of all duplciates
    """

    sels = cmds.ls(sl=True) #returns a list, string array ,['ball_geo', 'car_geo,
    all_dups = []
    for s in sels: # will go through each item and assign to s
        for n in range(num_of_duplicates):
            dup = cmds.duplicate(s, rr=True)[0] #will return ['ball_geo1']
            pos_x = random.uniform(min_x, max_x)
            pos_y = random.uniform(min_y, max_y)
            pos_z = random.uniform(min_z, max_z)

        cmds.xform(dup, worldSpace=True, translation=[pos_x, pos_y, pos_z])
        all_dups.append(dup)

    cmds.select(all_dups, replace=True)
    return all_dups
        #extend= will add each character. List of items to add.     append= good for strings


