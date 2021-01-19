import maya.cmds as cmds
# create a locator at the center of the current selection

    # first make selection in scene
    # get selection and assign to variable
    # get each individual component ?optional
    # find center point of selections
    # create a locator
    # assign the position of locator

def create_locator():
  sels = cmds.ls(sl = True)

  bbox = cmds.exactWorldBoundingBox(sels) #boundingbox = command (objects)
  x_pos = (bbox[0] + bbox[3])/2 #xmin,ymin,zmin,xmax,ymax,zmax. THIS IS XMIN,XMAX
  y_pos = (bbox[1] + bbox[4])/2 #ymin, ymax
  z_pos = (bbox[2] + bbox[5])/2 #xmin,xmax

  locator = cmds.spaceLocator(position = [0,0,0])[0]
  cmds.xform(locator, worldSpace = True, translation = [x_pos, y_pos, z_pos]) #move locator into place

  cmds.select(locator, r=True)

  return locator
