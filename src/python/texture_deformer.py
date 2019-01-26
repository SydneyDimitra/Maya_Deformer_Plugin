import maya.cmds as cmds

filepath = "icons/heightmap.png"

class TextureDeformer():
  """ """
  def __init__(self):
  """ """
  
  def get_object():
    
  def import_image():
  
  def match_resolution():
  
  def apply_deformation(max_height):
    """ max_height = 1 default value """


#####################################

plane = cmds.ls(selection = True)

# read image
from PIL import Image
im=Image.open(filepath)
print im.size 
x, y = im.size

# resolution
cmds.setAttr("polyPlane1.subdivisionsWidth", x)
cmds.setAttr("polyPlane1.subdivisionsHeight", y)

# read image pixel values
pixel_values = list(im.getdata())
#print len(pixel_values)
#print max(pixel_values)


# deformation
for i range(10):
    for value in pixel_values:
        cmds.setAttr("pPlaneShape1.pnts[{0}].pnty".format(i), value)
