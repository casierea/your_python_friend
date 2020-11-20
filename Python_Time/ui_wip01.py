import maya.cmds as cmds
my_window = 'CasieToolWindow2'
#formlayout
#look under controls for button,sliders,what you will need.



if cmds.window(my_window, exists=True):
    cmds.deleteUI(my_window)

my_window = cmds.window(my_window,
                        title='Super Cool Tool Window',
                        widthHeight=(200,200)) #creates window. Grandaddy. Main parent

col_layout = cmds.columnLayout(parent=my_window)
cmds.button(parent=col_layout)
cmds.button(parent=col_layout)

cmds.showWindow(my_window,)

#rename tool. Window- for a string. hit  button and do somthing with it.