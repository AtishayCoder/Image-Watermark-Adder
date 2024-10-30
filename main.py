from PIL import Image, ImageDraw, ImageFont

img_path = input("Enter full path to image: ")
water_mark_txt = input("Enter watermark text: ")

# get an image
with Image.open(img_path).convert("RGBA") as base:

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((50, 50), water_mark_txt, font=fnt, fill=(255, 255, 255, 128))

    out = Image.alpha_composite(base, txt)

    out.show()
