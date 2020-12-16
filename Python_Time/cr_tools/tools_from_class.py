import maya.cmds as cmds


def create_snowman(): #script that does a thing here in tools
    base_sphere = cmds.polySphere(r=1, sx=20, sy=20, ax=[0,1,0], cuv=2, cho=0)[0]
    cmds.setAttr('%.translateY' % base_sphere, 1) # % = will be inserting a string
    second_sphere = cmds.duplicate(base_sphere, rr=True)[0] #[0] return first object
    cmds.move(0, 1.35, 0, second_sphere, r=True)
    cmds.scale(.675, .675, .675, second_sphere, r=True)
    third_sphere = cmds.duplicate(second_sphere, rr=True)[0]
    cmds.scale(.7, .7, .7, third_sphere, r=True)
    cmds.move(0, 0.93097, 0, third_sphere, r=True)

def rename_geo(newest_name):
    sels = cmds.sel(sl=True)

    #for sel in sels:
       #cmds.rename(sel,'newest_name_Geo') # can do it like this

    for sel in sels:
        cmds.rename(sel, '%_Geo' % newest_name) #better like this

print "Hi"
#do not import tools_from_class. it is part of a package. Import cr_tools