import maya.cmds as cmds

class FreezeTransDelHist():
    def __init__(self):
        self.td_window = 'freeze trans ui'

    def create(self):
        self.delete()
        self.td_window = cmds.window(self.td_window,
                                     title='Freeze and Delete Window',
                                     widthHeight=(200, 400))  # creates window. Grandaddy. Main parent
        self.col_layout = cmds.columnLayout(parent=self.td_window,
                                            adjustableColumn=True)

        cmds.button(parent=self.col_layout, label='Freeze trans', c=lambda *x: self.call_freeze_trans())  # c=command)
        cmds.button(parent=self.col_layout, label='Del History', c=lambda *x: self.call_del_hist())

        cmds.showWindow(self.td_window)

    def delete(self):
        if cmds.window(self.td_window, exists=True):
            cmds.deleteUI(self.td_window)

    def call_freeze_trans(self, t=1, r=1, s=1, n=0, pn=1):
        selected_objs = cmds.ls(selection=True)
        for obj in selected_objs:
            cmds.makeIdentity(apply=True, t=t, r=r, s=s, n=n, pn=pn)


    def call_del_hist(self):
        selected_objs = cmds.ls(selection=True)
        for obj in selected_objs:
            cmds.delete(constructionHistory=True)


my_window = FreezeTransDelHist()
my_window.create()