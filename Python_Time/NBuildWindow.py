import maya.cmds as cmds
class RenamerUI():#WINDOWASSIGNMENT
    def __init__(self):
        self.my_window = 'crWindowTool_Renamer'

    def create(self):
        self.delete()
        self.my_window = cmds.window(self.my_window,
                                title='Super Boop Tool Window',
                                widthHeight=(200,200)) #creates window. Grandaddy. Main parent

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        self.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...') #creates a space to type in a string
        #name_field is the name of control. Not value contained in that field.

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

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



