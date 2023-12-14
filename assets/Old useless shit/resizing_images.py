import os
from PIL import Image


image = Image.open("background.png")
image = image.resize((800, 600))
image.save("background_rs.png", "png")
image.close()
