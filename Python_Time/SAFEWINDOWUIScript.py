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

        cmds.button(parent=self.col_layout, label='Activate', c='print "Activate the Function"') #c=command)

        cmds.button(parent=self.col_layout, label='Cube', c=self.createCube)

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)
    #def runCreateSpehere(self):
        #self.createSphere()

    #def createSphere(self, name):
        #field_value = cmds.textField(self.name_field, q=True, text=True)
        #cmds.polySphere(name=field_value)

    def createCube(self, name):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        cmds.polyCube(name=field_value)

    #def createTorus(self, name):
        #field_value = cmds.textField(self.name_field, q=True, text=True)
        #cmds.polyTorus(name=field_value)

        cmds.showWindow(self.my_window)

    #def SayHello():
        #print"Hello"
        #return 3

my_window = RenamerUI() #remove from script when done
my_window.create()