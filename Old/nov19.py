import maya.cmds as cmds
#build window for renamer and window for random placement generator
class RenamerUI():
    def init (self):
        self.my_window = 'crCoolToolWindow'
    def create(self):
        self.delete()

        self.my_window = cmds(self.my_window,
                              title='SuperCoolToolWindow,',
                              widthHeight=(200, 200))

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        self.name_field = cmds.textField(parent=self.col_layout,
                                         placeholderText='Name of new object...')
        self.size_slider = cmds.intSlider(parent=self.col_layout,
                                          minValue=0,
                                          maxValue=25)

        cmds.button(parent=self.col_layout, label='Sphere', c=lambda *x:self.createSphere())
        cmds.button(parent=self.col_layout, label='Sphere', c=lambda *x: self.createCube())
        cmds.button(parent=self.col_layout, label='Sphere', c=lambda *x: self.createTorus())
        cmds.button(parent=self.col_layout, label='Print field')


        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exist=True):
            cmds.delteUI(self.my_window)

    def createSphere(self):
        field_value = cmds.textField(self.name_fiel, q=True, text=True)
        size_value = cmds.intSlider(self.size_slider, q=True, value=True)
        cmds.polySphere(name=field_value, r=size_value)

    def createCube(self):
        field_value = cmds.textField(self.name_field, q=True, text=True)
        size_value = cmds.intSliderGrp(self.size_slider, q=True, value=True)
        cmds.polyCube(name=field_value, width=size_value, height=size_value, depth=size_value)

    def createToru(self):
        pass

    #my_window = RenamerUI()

    #my_window.create()








#class time
def SayHello():
    print "hello"
    return 3

SayHello()

lambda *x: print "hello"