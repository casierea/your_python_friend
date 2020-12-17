import maya.cmds as cmds


class Toolbox_UI():#class=capital letter camelcase# SCRIPT TO WORK ON
    def __init__(self):
        self.my_window = 'cr_mytools_ui'

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                title='cr_ToolBox',
                                widthHeight=(200,200)) #creates window. Grandaddy. Main parent

        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        #elf.name_field = cmds.textField(parent=self.col_layout, placeholderText='Name of new object...') #creates a space to type in a string
        #name_field is the name of control. Not value contained in that field.

        #cmds.button(parent=self.col_layout, label='Renamer', c=self.call_renamerUI()) #c=command)
        #cmds.button(parent=self.col_layout, label='Cube', c=self.call_snowman())


        cmds.button(parent=self.col_layout, label='Renamer UI', c=lambda *x: self.call_renamerUI())  # c=command)
        cmds.button(parent=self.col_layout, label = 'Random Gen Ui', c=lambda *x: self.call_randomer())




        cmds.button(parent=self.col_layout, label='Snowman', c=lambda *x: self.call_snowman())

        #cmds.button(parent=self.col_layout, label='Cube', c=lambda *x: self.createCube())
        cmds.showWindow(self.my_window)


    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)


    def call_renamerUI(self):
        import Rename_Window_UI #import script/module we need
        reload(Rename_Window_UI)
        renamerUI_instance = Rename_Window_UI.RenamerUI() #name you pick = script.class
        renamerUI_instance.create()
        print 'boop'


    def call_randomer(self):
        import RandomGen_Window_UI
        reload(RandomGen_Window_UI)
        randomerUI_instance = RandomGen_Window_UI.RandomUI
        randomerUI_instance.create()




    def call_snowman(self):
        import tools_from_class
        reload(tools_from_class)
        tools_from_class.create_snowman()


my_window = Toolbox_UI()
my_window.create()