# Standart imports
import maya.cmds as cmds
from PIL import Image
  
#filepath = "icons/heightmap.png"

class ImageReader():
  """Apply deformer to objects"""
  def __init__(self):
    """Class constructor."""
    self.input_resolution = None
    self.output_resolution = None
    self.pixel_values = None
 
  def read_image(self, filepath):
    """Import image from provided filepath.
    Args:
      filepath (str)
    Returns:
    """
    im=Image.open(filepath)
    x, y = im.size
    self.pixel_values = list(im.getdata())

  def normalise_pixel_values(self)
    """Normalise pixel values between 0 and 1. 
    Returns:
      normalised_vlaues (list):
    """
    # clamping the values between 0 and 1
    normalised_values = []
    max_pixel_value = max(self.pixel_values)
    for value in pixel_values:
        scaled_value = value / max_pixel_value
        normalised_values.append(scale_value)       
    return normalised_values
    
class MeshDeformer():
  """Apply deformer to object."""
  def __init__(self):
    """Class constructor."""
    self.width_subdivision = None
    self.height_subdivision = None
  
  def match_resolution(self,x,y):
    """Match mesh subdivision with image resolution."""

    cmds.setAttr("polyPlane1.subdivisionsWidth", x)
    cmds.setAttr("polyPlane1.subdivisionsHeight", y)
  
  def apply_deformation(self, max_height=1, normalised_values):
    """Apply deformation.
    Args:
      max_height (float):
    """
    i = 0
    for value in normalised_values:
        cmds.setAttr("pPlaneShape1.pnts[{0}].pnty".format(i), value * max_height)
        i += 1

    
def main(filepath, max_height):
  """Gets user inputs and connects deformer.
  Args:
    filepath (str):
    max_height (float):
  """
  plane = cmds.ls(selection = True)
  # check if polygon
  image = ImageReader()
  x,y = image.read_image()
  
  plane = MeshDeformer()
  plane.match_resolution(x,y)
  plane.apply_deformation(max_height, image.normalise_pixel_values())
  
  
