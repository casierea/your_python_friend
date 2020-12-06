
import maya.cmds as cmds
import random
class RandomPlacement():#WINDOWASSIGNMENT
    def __init__(self):
        self.my_window = 'crWindowTool_Renamer'

    def create(self):
        self.delete()
        self.my_window = cmds.window(self.my_window,
                                title='Super Boop Tool Window',
                                widthHeight=(200,200)) #creates window. Grandaddy. Main parent

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        cmds.text(label = "number of duplicate", parent = self.col_layout)
        self.dup_field = cmds.intField(parent=self.col_layout)
        cmds.text(label="X Min", parent=self.col_layout)
        self.X_Min_field = cmds.intField(parent=self.col_layout)
        cmds.text(label = "X Max", parent = self.col_layout)
        self.X_Max_field = cmds.intField(parent=self.col_layout)
        cmds.text(label = "Y Min", parent = self.col_layout)
        self.Y_Min_field = cmds.intField(parent=self.col_layout)
        cmds.text(label = "Y Max", parent = self.col_layout)
        self.Y_Max_field = cmds.intField(parent=self.col_layout)
        cmds.text(label = "Z Min", parent = self.col_layout)
        self.Z_Min_field = cmds.intField(parent=self.col_layout)
        cmds.text(label = "Z Max", parent = self.col_layout)
        self.Z_Max_field = cmds.intField(parent=self.col_layout)
        cmds.showWindow(self.my_window)

        cmds.button(parent=self.col_layout, label='Random', c=lambda * x:self.randomer())
        cmds.showWindow(self.my_window)
    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def duplicate_obj(self):

        if len(objects) < 1:
            print()
            print("no objects passed, using Maya selection from UI")
            objects = cmds.ls(selection=True)  # creating a list of selected objs

        if debug:  # if debug=True
            print(len(objects), "items length")
            print(objects)

        obj_returns = []  # list to hold names of objects that were duplicated

        for i in range(0, len(objects)):
            for j in range(0, num_copies):
                print("copying object {obj} copy number: {copy} of {total_copies} total copies".format(obj=objects[i],
                                                                                                       copy=j,
                                                                                                       total_copies=num_copies))
                cmds.xform(cmds.duplicate(objects[i]),
                           translation=[random.uniform(minX, maxX),
                                        random.uniform(minY, maxY),
                                        random.uniform(minZ, maxZ)])

            obj_returns.append(objects[i])

        return obj_returns

    duplicated_objects = duplicate_obj()
    def Renamer(self):
        sels = cmds.ls(selection = True)

    input_selection = 1
    TextNameString = cmds.textField(self.name_field, q=True, text=True)

    for sel in sels:

        collection_count = input_string.count('#')

        tupple_parts = input_string.partition('#' * collection_count)

        numbering_systems = str(input_selection)

        if tupple_parts[1]:
            print 'characters are good.'
            replace_zeroes = numbering_systems.zfill(3)

            cmds.rename(tupple_parts[0] + replace_zeroes + tupple_parts[2])

        else:

            cmds.error('characters are not in order. try again.')
        input_selection += 1

my_window = RenamerUI() #remove from script when done
my_window.create()



