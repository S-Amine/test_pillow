from PIL import Image

def get_center(image, bg, x_margin=0, y_margin=0):
    # x_margin & y_margin are used to readjust x & y parameters if needed
    center = (int( (bg.width - image.width) / 2) + x_margin , int( (bg.height - image.height) / 2) + y_margin)
    return center

background = Image.new("RGB", (1000,1000), (255, 255, 255))
vase = Image.open("vase.png")
flower = Image.open("flower.png")

background.paste(flower, get_center(flower, background, y_margin=-250, x_margin=50), flower)
background.paste(vase, get_center(vase, background, y_margin=150), vase)

background.show()
