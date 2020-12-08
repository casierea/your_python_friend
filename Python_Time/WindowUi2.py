import maya.cmds as cmds
class RenamerUI():#class=capital letter camelcase
    def __init__(self):
        self.my_window = 'crWindowTool'

    def create(self):
        self.delete()
        self.my_window = cmds.window(self.my_window,
                                title='Super Boop Tool Window',
                                widthHeight=(200,200)) #creates window. Grandaddy. Main parent

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        self.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...') #creates a space to type in a string
        #name_field is the name of control. Not value contained in that field.

        cmds.button(parent=self.col_layout, label='Hi', c='print "hello"') #c=command)
        cmds.button(parent=self.col_layout, label='Sphere', c=self.createSphere)
        #cmds.button(parent=self.col_layout, label='Sphere', c=self.SayHello)
        cmds.button(parent=self.col_layout, label='Taurus', c=self.createTorus)
        cmds.button(parent=self.col_layout, label='Cube', c=self.createCube)
        cmds.button(parent=self.col_layout, label='Print field',
                    c='print cmds.textField(name_field, q=True, text=True)') #print statement in output
        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)
    def runCreateSpehere(self):
        self.createSphere()

    def createSphere(self, name):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        cmds.polySphere(name=field_value)

    def createCube(self, name):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        cmds.polyCube(name=field_value)

    def createTorus(self, name):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        cmds.polyTorus(name=field_value)

        cmds.showWindow(self.my_window)

    def SayHello():
        print"Hello"
        return 3

my_window = RenamerUI() #remove from script when done
my_window.create()