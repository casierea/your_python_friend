import maya.cmds as cmds
import random



import maya.cmds as cmds

def duplicate_obj(objects=[], num_copies=1, minX=0, maxX=10, minY=0, maxY=10, minZ=0, maxZ=10, debug=True):

	if len(objects) < 1:
		print()
		print("no objects passed, using Maya selection from UI")
		objects = cmds.ls(selection=True) #creating a list of selected objs

	if debug:  #if debug=True
		print(len(objects), "items length")
		print(objects)

	obj_returns = [] #list to hold names of objects that were duplicated

	for i in range(0, len(objects)):
		for j in range(0, num_copies):
			print("copying object {obj} copy number: {copy} of {total_copies} total copies".format(obj=objects[i], copy=j, total_copies=num_copies))
			cmds.xform(cmds.duplicate(objects[i]),
					   translation=[random.uniform(minX, maxX),
									random.uniform(minY, maxY),
									random.uniform(minZ, maxZ)])

		obj_returns.append(objects[i])

	return obj_returns

duplicated_objects = duplicate_obj()