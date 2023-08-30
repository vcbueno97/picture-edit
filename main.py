from PIL import Image

with Image.open("cn vs bhs.png") as im: 
    px = im.load()

for x in range(im.size[0]):
    for y in range(im.size[1]):
        px[x, y] = (0, 0, 0)

im.show()
