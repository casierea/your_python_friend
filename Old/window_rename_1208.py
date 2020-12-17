import maya.cmds as cmds
class RenamerUI():
    def __int_(self):  # 2 underscores
        self.my_window = 'crWindowTool'

    def create(self):
        self.delete()
        self.my_window = cmds.window(self.window,
                                     title='Super Cool Tool Window',
                                     widthHeight=(200, 200))  # creates window. Grand daddy of them all.
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        self.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...')

        cmds.button(parent=self.col_layout, label='Hi', c='print "hello"')  # c=command)
        cmds.button(parent=self.col_layout, label='Sphere', c=self.createSphere)
        # cmds.button(parent=self.col_layout, label='Sphere', c=self.SayHello)
        cmds.button(parent=self.col_layout, label='Taurus', c=self.createTorus)
        cmds.button(parent=self.col_layout, label='Cube', c=self.createCube)
        cmds.button(parent=self.col_layout, label='Print field')  # c=command)


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



my_window = RenamerUI()  # remove from script when done
my_window.create()

