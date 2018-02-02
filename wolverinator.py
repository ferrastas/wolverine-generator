# 'WOLVERINE CRUSH' meme generator
# JS Kouri
# 8/2014
# No restrictions on use

from PIL import Image
import hashlib
import time
import os

def file_name():
  # Generate unique file name (variable 'name') based on hash of time
  global name
  t = time.time()
  h = hashlib.md5()
  h.update(str(t).encode("utf8"))
  name = str(h.hexdigest())
  name = name[0:5] + ".png"

''' Note: I hate sequential file names and I keep forgetting the syntax of the hashlib library, hence this odd naming scheme method. It's personally useful to me for memorizing syntax with repeat exposure.  '''
 
  
file_name()

# open base image and image to be superimposed:
wolverine = Image.open("/code/media/wolverine_generator.png")
user_img = Image.open(os.environ['IMG_PATH'])


# rotate user image to match angle of picture frame, preserve quality with bicubic interpolation
user_img.thumbnail((280,320))
rot = user_img.rotate(6, resample=Image.BICUBIC, expand=1)


# create a new empty image with alpha, set to base (wolverine) image size
new_im = Image.new('RGBA', (480,700))


# paste rotated user image first, paste base image with alpha in picture frame second
new_im.paste(rot, (120,350) )
new_im.paste(wolverine, (0,0), mask=wolverine)


# save
#location = os.environ['DEST_PATH'] + "/" + name
location = os.environ['DEST_PATH'] + "/latest.png"
new_im.save(location)