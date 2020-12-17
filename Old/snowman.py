import maya.cmds as cmds

def create_snowman():
    base_sphere = cmds.polySelectSp(r=1, sx=20, sy=20, ax=[0,1,0], cuv=2, ch=0)[0]
    cmds.setAttr('%s.translateY' % base_sphere, 1)
    second_sphere = cmds.duplicate(base_sphere, rr=True)[0]
    cmds.move(0, 1.35, 0, second_sphere, r =True)
    cmds.scale(.674, .675, .675, second_sphere, r=True)
    third_sphere = cmds.duplicate(second_sphere, rr=True)
    cmds.scale(.7, .7, .7, third_sphere, r=True)
    cmds.move(0, 0.93097, 0, third_sphere, r=True)
def rename_geo(new_name):
    sels = cmds.sel(sl=True)

    for sel in sels:
        cmds.rename(sel, '%s_Geo' % new_name)


