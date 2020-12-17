import maya.cmds as cmds

class ParentGroup():#class=capital letter camelcase# SCRIPT TO WORK ON
    def __init__(self):
        self.pg_window = 'crParentGroupUI'

    def create(self):
        self.delete()
        self.pg_window = cmds.window(self.pg_window,
                                     title='ParenGroupWindow',
                                     widthHeight=(200, 400))  # creates window. Grandaddy. Main parent
        self.col_layout = cmds.columnLayout(parent=self.pg_window,
                                            adjustableColumn=True)

        #self.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...') #creates a space to type in a string
        #name_field is the name of control. Not value contained in that field.

        cmds.button(parent=self.col_layout, label='parent grouping', c=lambda *x: self.call_pg_window())

        cmds.showWindow(self.pg_window)

    def delete(self):
        if cmds.window(self.pg_window, exists=True):
            cmds.deleteUI(self.pg_window)

    def call_pg_groupa(self):
        selected_objs = cmds.ls(selection=True)

        for obj in selected_objs:
            pg = cmds.group(em=True)
            cmds.parent(obj, pg)


my_window = ParentGroup()
my_window.create()