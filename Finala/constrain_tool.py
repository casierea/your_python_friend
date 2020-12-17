import maya.cmds as cmds
class ConstrainerUI():#class=capital letter camelcase# SCRIPT TO WORK ON
    def __init__(self):
        self.my_window = 'constwindow'

    def create(self):
        self.delete()
        self.constwindow = cmds.window(self.constwindow,
                                       title='Reconstrainer window tool',
                                       widthHeight=(200,200)) #creates window. Grandaddy. Main parent

        self.col_layout = cmds.columnLayout(parent=self.constwindow,
                                            adjustableColumn=True)

        #self.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...') #creates a space to type in a string
        #name_field is the name of control. Not value contained in that field.

        cmds.button(parent=self.col_layout, label='Constrainer', c=self.constwindow) #c=command)
        #cmds.button(parent=self.col_layout, label='Cube', c=self.constwindow)

        cmds.showWindow(self.constwindow)

    def delete(self):
        if cmds.window(self.constwindow, exists=True):
            cmds.deleteUI(self.constwindow)



    def call_constrainer(self):
        pass
        #selected_objs = cmds.ls(selection=True)


