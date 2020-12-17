import maya.cmds as cmds
class RenamerUI():# SCRIPT TO WORK ON
    def __init__(self):
        self.my_window = 'crWindowRENAMERTool'

    def create(self):
        self.delete()
        self.my_window = cmds.window(self.my_window,
                                title='Renamer Window',
                                widthHeight=(200,200)) #creates window. Grandaddy. Main parent

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        self.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...') #creates a space to type in a string


        cmds.button(parent=self.col_layout, label='Activate', c='print "Activate the Function"') #c=command)

        cmds.button(parent=self.col_layout, label='Cube', c=self.createCube)

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def renamer(self):
        def rename_stuffles(name_base="Leg_###_Jnt", index_start=0):

            # error message for bad string format
            if name_base.count("_") != 2:
                print("""invalid name base string entered.
                    \n Please enter name_base with format: part_###_node""")
                return

            print("\n\n")
            # create list to hold renamed objs
            renamed_objs = []

            # get objects in selection
            sel_objs = cmds.ls(selection=True)  # ["billy", "turkey", "stuffin"]
            print(type(sel_objs))
            print(len(sel_objs))
            print("selection objects:", sel_objs)
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

        rename_stuffles(index_start=1)
        # rename_stuffles(name_base="boop_#######_bop")





    def createCube(self, name):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        cmds.polyCube(name=field_value)



        cmds.showWindow(self.my_window)



my_window = RenamerUI() #remove from script when done
my_window.create()