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

        cmds.button(parent=self.col_layout, label ='Renamer UI', c=lambda *x: self.call_renamerUI())  # c=command)
        cmds.button(parent=self.col_layout, label = 'Random Gen Ui', c=lambda *x: self.call_randomer())
        cmds.button(parent=self.col_layout, label = 'Freeze trans', c=lambda *x: self.call_freeze_trans())  # c=command)
        cmds.button(parent=self.col_layout, label = 'Del History', c=lambda *x: self.call_del_hist())
        cmds.button(parent=self.col_layout, label='Parent Group it', c=lambda *x: self.call_pg_groupa())

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
        randomerUI_instance = RandomGen_Window_UI.RandomUI()
        randomerUI_instance.create()

    def call_freeze_trans(self):
        import freeze_trans_delete_hist
        reload(freeze_trans_delete_hist)
        freezerUI_instance = freeze_trans_delete_hist.FreezeTransDelHist()
        freezerUI_instance.call_freeze_trans()

    def call_del_hist(self):
        import freeze_trans_delete_hist
        reload(freeze_trans_delete_hist)
        deleterUI_instance = freeze_trans_delete_hist.FreezeTransDelHist()
        deleterUI_instance.call_del_hist()

    def call_pg_groupa(self):
        import parent_group
        reload(parent_group)
        pg_instance = parent_group.ParentGroup()
        pg_instance.call_pg_groupa()


my_window = Toolbox_UI()
my_window.create()