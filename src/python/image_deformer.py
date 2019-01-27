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

# clamping the values between 0 and 1
clamped_values = []
max_pixel_value = max(pixel_values)
for value in pixel_values:
    scaledValue = value / max_pixel_value
    clamped_values.append(scaleValue)

# deformation
i = 0
for value in pixel_values:
    cmds.setAttr("pPlaneShape1.pnts[{0}].pnty".format(i), value * max_height)
    i += 1
    
