from PIL import Image,ImageDraw
import math, operator

dots = 25 #size of squares to slice

def image_diff(image1,image2,output):
  """ Returns a third image that highlights the difference between two images.
      The third image will be a copy of the first image, with differences outlined in red.
      If the images are identical, this will return None
  """

  width,height = image1.size
  rows = height/dots
  cols = width/dots

  #lists of rows and columns that are different
  diff_ir = []
  diff_ic = []

  for ir in range(rows):
    for ic in range(cols):
      box = (dots*ic,dots*ir,dots*(ic+1),dots*(ir+1))
      h1 = image1.crop(box).histogram()
      h2 = image2.crop(box).histogram()

      rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
      if rms:
        diff_ir.append(ir)
        diff_ic.append(ic)

  if diff_ir and diff_ic:
    box = (
      (min(diff_ic)*dots,min(diff_ir)*dots),
      (max(diff_ic)*dots+dots,max(diff_ir)*dots+dots)
      )
    draw = ImageDraw.Draw(image1)
    for i in range(3):
      draw.rectangle(box,**{'outline':'#FF0000'})
      box = (
        (box[0][0]-1,box[0][1]-1),
        (box[1][0]+1,box[1][1]+1),
        )
  image1.save(output,"PNG")

if __name__ == "__main__":
  image_diff('i1.png','i2.png','output.png')
