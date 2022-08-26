from PIL import Image

def get_center(image, bg, x_margin=0, y_margin=0):
    # x_margin & y_margin are used to readjust x & y parameters if needed
    center = (int( (bg.width - image.width) / 2) + x_margin , int( (bg.height - image.height) / 2) + y_margin)
    return center
 

background = Image.new("RGB", (2080,2080), "white")
removed_white=Image.new("RGB", (100,100), "white")
vase = Image.open("vase.png")

vase2 = Image.open("vase2.png")
flower = Image.open("flower.png")
flower2 = Image.open("rose2.png")
flower3 = Image.open("rose3.png")
flower4 = Image.open("rose4.png")
topc5 = Image.open("topc5.png")


background.paste(flower3.rotate(0,translate=(50,50),resample=Image.Resampling.BICUBIC), get_center(flower3, background, y_margin=-200, x_margin=-15), flower3.rotate(0,translate=(50,50),resample=Image.Resampling.BICUBIC))
background.paste(flower3.rotate(20,translate=(50,50),resample=Image.Resampling.BICUBIC), get_center(flower3, background, y_margin=-70, x_margin=-15), flower3.rotate(20,translate=(50,50),resample=Image.Resampling.BICUBIC))
background.paste(flower.rotate(-20,translate=(50,50),resample=Image.Resampling.BICUBIC), get_center(flower, background, y_margin=-70, x_margin=-30), flower.rotate(-20,translate=(50,50),resample=Image.Resampling.BICUBIC))
background.paste(flower.rotate(20,translate=(50,50),resample=Image.Resampling.BICUBIC), get_center(flower, background, y_margin=-70, x_margin=-15), flower.rotate(20,translate=(50,50),resample=Image.Resampling.BICUBIC))
background.paste(flower4.rotate(20,translate=(50,50),resample=Image.Resampling.BICUBIC), get_center(flower, background, y_margin=-70, x_margin=-15), flower4.rotate(20,translate=(50,50),resample=Image.Resampling.BICUBIC))
background.paste(flower4.rotate(-20,translate=(50,50),resample=Image.Resampling.BICUBIC), get_center(flower, background, y_margin=-70, x_margin=-15), flower4.rotate(-20,translate=(50,50),resample=Image.Resampling.BICUBIC))
background.paste(topc5.rotate(0,translate=(50,200),resample=Image.Resampling.BICUBIC), get_center(topc5, background, y_margin=-200, x_margin=-10), topc5.rotate(0,translate=(50,200),resample=Image.Resampling.BICUBIC))

background.paste(flower.rotate(0,translate=(50,100),resample=Image.Resampling.BICUBIC), get_center(flower, background, y_margin=-70, x_margin=-15), flower.rotate(0,translate=(50,100),resample=Image.Resampling.BICUBIC))

""" background.paste(flower, get_center(flower, background, y_margin=-80, x_margin=60), flower)
background.paste(flower2.rotate(-10), get_center(flower2, background, y_margin=-50, x_margin=60), flower2.rotate(-10))
background.paste(flower2.rotate(-20), get_center(flower2, background, y_margin=-50, x_margin=60), flower2.rotate(-20))
background.paste(flower2.rotate(15), get_center(flower2, background, y_margin=-50, x_margin=60), flower2.rotate(15))
background.paste(flower2.rotate(-13), get_center(flower2, background, y_margin=-50, x_margin=60), flower2.rotate(-13))
background.paste(flower2.rotate(-18), get_center(flower2, background, y_margin=-50, x_margin=60), flower2.rotate(-18))
background.paste(flower.rotate(20), get_center(flower, background, y_margin=-50, x_margin=40), flower.rotate(20))
background.paste(flower.rotate(2), get_center(flower, background, y_margin=-50, x_margin=40), flower.rotate(2)) """


background.paste(vase, get_center(vase, background, y_margin=130,x_margin=70), vase)


background.show()

