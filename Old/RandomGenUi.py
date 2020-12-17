import random

import maya.cmds as cmds



class RandomUI():# SCRIPT TO WORK ON
    def __init__(self, debug=True):
        self.my_window = 'cr_GenerateRandom'
        self.debug=debug

    def create(self):
        self.delete()
        self.my_window = cmds.window(self.my_window,
                                title='Random Generate Window',
                                widthHeight=(400,800)) #creates window. Grandaddy. Main parent

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        cmds.text(label="number of duplicate", parent=self.col_layout)
        self.dup_field = cmds.intField(parent=self.col_layout)

        cmds.text(label="X Min", parent=self.col_layout)
        self.X_Min_field = cmds.intField(parent=self.col_layout)

        cmds.text(label="X Max", parent=self.col_layout)
        self.X_Max_field = cmds.intField(parent=self.col_layout)

        cmds.text(label="Y Min", parent=self.col_layout)
        self.Y_Min_field = cmds.intField(parent=self.col_layout)

        cmds.text(label="Y Max", parent=self.col_layout)
        self.Y_Max_field = cmds.intField(parent=self.col_layout)

        cmds.text(label="Z Min", parent=self.col_layout)
        self.Z_Min_field = cmds.intField(parent=self.col_layout)

        cmds.text(label="Z Max", parent=self.col_layout)
        self.Z_Max_field = cmds.intField(parent=self.col_layout)


        self.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...') #creates a space to type in a string


        cmds.button(parent=self.col_layout, label='Activate', c='print "Activate the Function"') #c=command)

        cmds.button(parent=self.col_layout, label='Cube', c=self.createCube)
        cmds.button(parent=self.col_layout, label='Random Gnerator', c=self.duplicate_obj)  # c=command)
        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def createCube(self, name):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        cmds.polyCube(name=field_value)

    def duplicate_obj(self, boop):


        minX = cmds.intField(self.X_Min_field, q=True, value=True)
        maxX = cmds.intField(self.X_Max_field, q=True, value=True)

        minY = cmds.intField(self.Y_Min_field, q=True, value=True)
        maxY = cmds.intField(self.Y_Max_field, q=True, value=True)

        minZ = cmds.intField(self.Z_Min_field, q=True, value=True)
        maxZ = cmds.intField(self.Z_Max_field, q=True, value=True)
        num_copies = cmds.intField(self.dup_field, q=True, value=True)
        objects = cmds.ls(selection=True)  # creating a list of selected objs

        if self.debug:  # if debug=True
            print(len(objects), "items length")
            print(objects)

        obj_returns = []  # list to hold names of objects that were duplicated

        for i in range(0, len(objects)):
            for j in range(0, num_copies):
                print(
                    "copying object {obj} copy number: {copy} of {total_copies} total copies".format(obj=objects[i],
                                                                                                     copy=j,
                                                                                                     total_copies=num_copies))
                cmds.xform(cmds.duplicate(objects[i]),
                           translation=[random.uniform(minX, maxX),
                                        random.uniform(minY, maxY),
                                        random.uniform(minZ, maxZ)])

            obj_returns.append(objects[i])

        return obj_returns