# importing image from PIL module
from PIL import Image

# opening the image from the current working directory
open_image = Image.open('minion.jpg')

convert_to_bw = open_image.convert('L')
# converting image to the black and white
convert_to_bw.show()
