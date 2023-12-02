from PIL import Image
from PIL import ImageOps
import sys

if len(sys.argv) != 3:
    sys.exit("format : python shirt.py before.jpg after.jpg")

exts = ["jpg","png","jpeg"]
if not(sys.argv[1].split(".")[1].lower() in exts and sys.argv[2].split('.')[1].lower() in exts):
    sys.exit("file format not supported")

if not (sys.argv[1].split(".")[1].lower() == sys.argv[2].split('.')[1].lower()):
    sys.exit("file format of output and input should be same")

image = Image.open(sys.argv[1])
shirt = Image.open("shirt.png")
size = shirt.size
image = ImageOps.fit(image, size)

image.paste(shirt,shirt)
image.save(sys.argv[2])
