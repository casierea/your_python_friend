import maya.cmds as cmds
my_window = 'CasieToolWindow3'
#formlayout
#look under controls for button,sliders,what you will need.

if cmds.window(my_window, exists=True):
    cmds.deleteUI(my_window)

my_window = cmds.window(my_window,
                        title='Awesome BlahBlah Tool Window',
                        widthHeight=(200,200)) #creates window. Grandaddy. Main parent

col_layout = cmds.columnLayout(parent=my_window, adjustableColumn=True)

name_field = cmds.textField(parent=col_layout, placeholderText='Name of new object...') #creates a space to type in a string
#name_field is the name of control. Not value contained in that field.

cmds.button(parent=col_layout, label='Hi', c='print "hello"') #c=command)

cmds.button(parent=col_layout, label='Sphere', c='createSphere()')

cmds.button(parent=col_layout, label='Taurus', c='createTorus()')

cmds.button(parent=col_layout, label='Cube', c='createCube()')

cmds.button(parent=col_layout, label='Print field',
            c='print cmds.textField(name_field, q=True, text=True)') #print statement in output

 #create polysphere


cmds.showWindow(my_window)


def createSphere():
    field_value = cmds.textField(name_field, q=True, text=True)
    cmds.polySphere(name=field_value)

def createCube():
    field_value = cmds.textField(name_field, q=True, text=True)
    cmds.polyCube(name=field_value)

def createTorus():
    field_value = cmds.textField(name_field, q=True, text=True)
    cmds.polyTorus(name=field_value)

cmds.showWindow(my_window)