"""
makes .ico files used for favico and such
based on: http://en.wikipedia.org/wiki/ICO_(file_format)

"""

import sys
from PIL import Image
from struct import Struct


icon_header = Struct("<xxHH")
image_header = Struct("<BBBxHHII")

buf = open(sys.argv[1], 'wb')

image_datas = []
images = []
for image in sys.argv[2:]:
    image_datas.append(open(image).read())
    images.append(Image.open(image))

buf.write(icon_header.pack(1, len(images)))
offset = icon_header.size + image_header.size * len(images)
for image, data in zip(images, image_datas):
    buf.write(image_header.pack(image.size[0], image.size[1], 0, 0, 0, len(data), offset))
    offset += len(data)

for data in image_datas:
    buf.write(data)

buf.close()
