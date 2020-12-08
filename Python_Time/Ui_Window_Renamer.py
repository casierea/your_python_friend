
import maya.cmds as cmds
class RenamerUI():
    def__init__(self)
        self.my_window = 'CasieToolWindow2'
    def create(self):
        self.delete()

    self.my_window = cmds.window(my_window,
                        title='Super Cool Tool Window',
                        widthHeight=(200,200)) #creates window. Grandaddy. Main parent
    self.col_layout = cmds.columnLayout(parent=self.my_window,
                                        adjustableColumn=True)
    self.name_field = cmds.textField(parent=self.col_layout,
                                     placeholderText='Name of new object...')

    cmds.button(parent=self.col_layout, label='Sphere', c='createSphere()')
    cmds.button(parent=self.col_layout, label='Cubee', c='cmds.polyCube()')
    cmds.button(parent=self.col_layout, label='Torus', c='cmds.polyTorus()')
    cmds.button(parent=self.col_layout, label='Print field',
                c='print cmds.textField(name_field, q=True, text=True)')
    cmds.ShowWindow(self.my_window)

def delete()