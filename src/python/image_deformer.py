# Standart imports
import maya.cmds as cmds
from PIL import Image
  
#filepath = "icons/heightmap.png"

class ImageDeformer():
  """Apply deformer to objects"""
  def __init__(self):
    """Class constructor."""
    self.resolution = None
  
  def get_object(self):
    """Get selected object.
    Returns:
    """
    plane = cmds.ls(selection = True)
    # check if polygon
 
  def import_image(self, filepath):
    """Import image from provided filepath.
    Args:
      filepath (str)
    Returns:
    """
    im=Image.open(filepath)
    x, y = im.size
    pixel_values = list(im.getdata())
  
  def match_resolution(self):
    """Match mesh subdivision with image resolution."""

    cmds.setAttr("polyPlane1.subdivisionsWidth", x)
    cmds.setAttr("polyPlane1.subdivisionsHeight", y)
  
  def apply_deformation(max_height=1):
    """Apply deformation.
    Args:
      max_height (float):
    """
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

    
def main(filepath, max_height):
  """Gets user inputs and connects deformer.
  Args:
    filepath (str):
    max_height (float):
  """
  deform = ImageDeformer()
  
  
