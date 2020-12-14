import maya.cmds as cmds


def create_snowman():
    base_sphere = cmds.polySphere(r=1, sx=20, sy=20, ax=[0,1,0], cuv=2, cho=0)[0]
    cmds.setAttr('%.translateY' % base_sphere, 1)
    second_sphere = cmds.duplicate(base_sphere, rr=True)[0]
    cmds.move(0, 1.35, 0, second_sphere, r=True)
    cmds.scale(.675, .675, .675, second_sphere, rr=True)
    third_sphere = cmds.duplicate(second_sphere, r=True)[0]
    cmds.scale(.7, .7, .7, third_sphere, r=True)
    cmds.move(0, 0.93097, 0, third_sphere, r=True)

def rename_geo(newest_name):
    sels = cmds.sel(sl=True)

    for sel in sels:
        cmds.rename(sel, '%_Geo' % newest_name)

print "Hi"