import maya.cmds as cmds
class RenamerUI():#class=capital letter camelcase# SCRIPT TO WORK ON
    def __init__(self):
        self.my_window = 'crRenameTool'

    def create(self):
        self.delete()
        self.my_window = cmds.window(self.my_window,
                                title='Renamer Window Tool',
                                widthHeight=(200,200)) #creates window. Grandaddy. Main parent

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        self.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...') #creates a space to type in a string
        #name_field is the name of control. Not value contained in that field.

        cmds.button(parent=self.col_layout, label='Renamer', c=self.renameInOrder) #c=command)
        cmds.button(parent=self.col_layout, label='Cube', c=self.createCube)
        cmds.showWindow(self.my_window)


    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def createCube(self, name):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        cmds.polyCube(name=field_value)



    def renameInOrder(self, index_start=0):

        #minX = cmds.intField(self.X_Min_field, q=True, value=True)
        name_base = cmds.textField(self.name_field, q=True)

        # error message for bad string format
        print (name_base)
        if name_base is None or len(name_base) < 1:
            name_base = "arm_###_jnt"
        #print(dir(self.name_field))
        if name_base.count("#") < 1:
            print("""invalid name base string entered.
                \n Please enter name_base with format: part_###_node""")
            return

        print("\n\n")
        # create list to hold renamed objs
        renamed_objs = []

        # get objects in selection
        sel_objs = cmds.ls(selection=True)  # ["billy", "turkey", "stuffin"]
        #print(type(sel_objs))
        #print(len(sel_objs))
        #print("selection objects:", sel_objs)
        # get count of # characters
        pounds = name_base.count("#")
        print("pounds: ", pounds)

        for i in range(0, len(sel_objs)):
            print(i, "*" * 50)
            print("base name string:", name_base)
            # split name base string on _ because it is a known pattern
            name_base_parts = name_base.split("_")
            print(name_base_parts)
            # 0 pad selection count to fill # characters properly
            part_count = str(i + index_start).zfill(pounds)
            print("count of # signs:", name_base.count("#"))
            # replace the # segment of the string, it will be the second item (index 1)

            name_base_parts[1] = part_count
            print("after substitution of # characters:", name_base_parts[1])

            # rejoin the string parts into the desired name
            new_name = "_".join(name_base_parts)
            print("new string name:", new_name)
            cmds.rename(sel_objs[i], new_name)
            # rename each object using the new name string
            # call rename function on sel_objs[i] here
            # add new obj name to renamed_objs list
            renamed_objs.append(new_name)
            print()
            print()
        return renamed_objs


my_window = RenamerUI() #remove from script when done
my_window.create()