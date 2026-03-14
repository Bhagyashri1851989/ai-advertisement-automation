from PIL import Image, ImageDraw

img = Image.new("RGB", (600,400), color="yellow")

draw = ImageDraw.Draw(img)
draw.text((150,180), "SPECIAL OFFER", fill="black")

img.save("poster.png")

print("Poster created!")
