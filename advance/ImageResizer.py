from PIL import Image

myimg = Image.open("Y:\All Photos\code-play-logo.png")

print(myimg.size)
# here we can reduce the size of image
# myimg = myimg.reduce([2,3])

height = int(input("Give height to this image: "))
width = int(input("Give length to this image: "))
# it will give the size that we gave
# myimg = myimg.resize((height, width))
# it will consider the size as thumbnail
myimg.thumbnail((height,width))
print(myimg.size)

myimg.show()
# we can save the image
# myimg.save("Y:\All Photos\code-play-logo2.png")
