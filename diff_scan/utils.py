from PIL import Image,ImageDraw
import math, operator

dots = 25 #size of squares to slice

def _is_diff(i1,i2):
  """Look at two PIL image objects and return True or False if they are different"""
  h1 = i1.histogram()
  h2 = i2.histogram()
  return math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

def image_diff(image1,image2,output):
  """ Returns a third image that highlights the difference between two images.
      The third image will be a copy of the first image, with differences outlined in red.
      If the images are identical, this will return None
  """

  image1 = Image.open(str(image1))
  image2 = Image.open(str(image2))

  width,height = image1.size
  rows = height/dots
  cols = width/dots

  if not _is_diff(image1,image2): #images are identical
    return

  image_d = image1.crop((0,0,width,height))
  image_d.mode = 'RGBA'
  draw = ImageDraw.Draw(image_d)
  poly = Image.new('RGBA', (dots,dots))
  pdraw = ImageDraw.Draw(poly)
  pdraw.rectangle((0,0,dots,dots),fill=(255,0,0,192))

  for ir in range(rows):
    box = (0,dots*ir,width,dots*(ir+1))
    if not _is_diff(image1.crop(box),image2.crop(box)):
      continue
    for ic in range(cols):
      box = (dots*ic,dots*ir,dots*(ic+1),dots*(ir+1))
      h1 = image1.crop(box).histogram()
      h2 = image2.crop(box).histogram()

      rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
      if rms:
        box = (
          ic*dots,ir*dots,
          ic*dots+dots,ir*dots+dots
          )
        image_d.paste(poly,box,poly) #draw.rectangle(box,fill=(255,0,0,64))
  image_d.save(output,"PNG")
  return True

if __name__ == "__main__":
  image_diff('i1.png','i2.png','output.png')
